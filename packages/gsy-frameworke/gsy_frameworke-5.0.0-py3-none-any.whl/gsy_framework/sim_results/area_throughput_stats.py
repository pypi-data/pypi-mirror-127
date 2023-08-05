"""
Copyright 2018 Grid Singularity
This file is part of D3A.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from typing import Dict
from gsy_framework.utils import round_floats_for_ui, create_subdict_or_update
from gsy_framework.sim_results.results_abc import ResultsBaseClass


class AreaThroughputStats(ResultsBaseClass):
    def __init__(self):
        self.results = {}
        self.results_redis = {}
        self.exported_energy = {}
        self.imported_energy = {}

    def update(self, area_result_dict=None, core_stats=None, current_market_slot=None):
        if not self._has_update_parameters(
                area_result_dict, core_stats, current_market_slot):
            return
        self.results = {}
        self.results_redis = {}
        self.update_results(area_result_dict, core_stats, current_market_slot)

    def update_results(self, area_dict, core_stats, current_market_time_slot_str):
        area_throughput = core_stats.get(area_dict['uuid'], {}).get('area_throughput', {})
        imported_peak = round_floats_for_ui(area_throughput.get('imported_energy_kWh', 0.))
        exported_peak = round_floats_for_ui(area_throughput.get('exported_energy_kWh', 0.))
        net_peak = round_floats_for_ui(imported_peak - exported_peak)
        import_peak_energy_net_kWh = net_peak if net_peak > 0 else 0.
        export_peak_energy_net_kWh = abs(net_peak) if net_peak < 0 else 0.
        area_results = {
            "import": {'peak_energy_trade_kWh': imported_peak,
                       "peak_energy_net_kWh": import_peak_energy_net_kWh},
            "export": {'peak_energy_trade_kWh': exported_peak,
                       "peak_energy_net_kWh": export_peak_energy_net_kWh},
            "net_energy_flow": {'peak_energy_kWh': net_peak}
        }

        baseline_import = area_throughput.get('baseline_peak_energy_import_kWh', None)
        baseline_export = area_throughput.get('baseline_peak_energy_export_kWh', None)
        if (baseline_import is not None and baseline_import > 0) or \
                (baseline_export is not None and baseline_export > 0):
            if baseline_import is not None and baseline_import > 0:
                peak_percentage = round_floats_for_ui(
                    area_results['import']['peak_energy_net_kWh'] / baseline_import * 100
                )
                area_results["import"].update(
                    {'peak_percentage': peak_percentage,
                     'baseline_peak_energy_kWh': round_floats_for_ui(baseline_import)}
                )
            if baseline_export is not None and baseline_export > 0:
                peak_percentage = round_floats_for_ui(
                    area_results['export']['peak_energy_net_kWh'] / baseline_export * 100
                )
                area_results["export"].update(
                    {'peak_percentage': peak_percentage,
                     'baseline_peak_energy_kWh': round_floats_for_ui(baseline_export)}
                )

        import_capacity = area_throughput.get('import_capacity_kWh', None)
        export_capacity = area_throughput.get('export_capacity_kWh', None)
        if import_capacity is not None and import_capacity > 0:
            area_results["import"].update(
                {'capacity_kWh': round_floats_for_ui(import_capacity)}
            )
        if export_capacity is not None and export_capacity > 0:
            area_results["export"].update(
                {'capacity_kWh': round_floats_for_ui(export_capacity)}
            )
        area_throughput_profile = {}
        area_throughput_profile[current_market_time_slot_str] = area_results

        create_subdict_or_update(self.results, area_dict['name'], area_throughput_profile)
        create_subdict_or_update(self.results_redis, area_dict['uuid'], area_throughput_profile)

        for child in area_dict['children']:
            if child['type'] == "Area":
                self.update_results(child, core_stats, current_market_time_slot_str)

    @staticmethod
    def merge_results_to_global(market_trade: Dict, global_trade: Dict, *_):
        if not global_trade:
            global_trade = market_trade
            return global_trade
        for area_uuid in market_trade:
            if area_uuid not in global_trade or global_trade[area_uuid] == {}:
                global_trade[area_uuid] = {}
            for time_slot in market_trade[area_uuid]:
                global_trade[area_uuid][time_slot] = market_trade[area_uuid][time_slot]
        return global_trade

    def restore_area_results_state(self, area_dict: Dict, last_known_state_data: Dict):
        pass

    @property
    def raw_results(self):
        return self.results

    @property
    def ui_formatted_results(self):
        return self.results_redis

    def memory_allocation_size_kb(self):
        return self._calculate_memory_allocated_by_objects([
            self.results, self.results_redis, self.imported_energy, self.exported_energy
        ])
