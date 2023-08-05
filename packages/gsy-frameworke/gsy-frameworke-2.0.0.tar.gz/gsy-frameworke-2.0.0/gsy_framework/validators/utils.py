"""
Copyright 2018 Grid Singularity
This file is part of D3A.

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If
not, see <http://www.gnu.org/licenses/>.
"""
import ast
from typing import Optional

from gsy_framework.constants_limits import ConstSettings
from gsy_framework.exceptions import GSyDeviceException

CepSettings = ConstSettings.CommercialProducerSettings


def validate_fit_to_limit(
        fit_to_limit: Optional[bool], energy_rate_increase_per_update: Optional[bool],
        energy_rate_decrease_per_update: Optional[bool]):
    """Check that fit_to_limit is correct when both energy rates changes are allowed.

    Important: don't use this method to validate devices that only accept one rate (e.g. Load and
    PV devices).
    """
    if fit_to_limit is True and (
            energy_rate_decrease_per_update is not None
            or energy_rate_increase_per_update is not None):
        raise GSyDeviceException({
            "misconfiguration": [
                "fit_to_limit and energy_rate_increase/decrease_per_update can't be set "
                "together."]})

    if fit_to_limit is False and (
            energy_rate_increase_per_update is None
            or energy_rate_decrease_per_update is None):
        raise GSyDeviceException(
            {"misconfiguration": [
                "energy_rate_increase/decrease_per_update must be set if fit_to_limit is "
                "False."]})


def validate_range_limit(initial_limit, value, final_limit, error_message):
    """Check that the provided arguments form a valid range."""
    if not initial_limit <= value <= final_limit:
        raise GSyDeviceException(error_message)


def validate_energy_rate(**kwargs):
    """Check that the provided energy rate is valid."""
    energy_rate = kwargs.get("energy_rate")
    if energy_rate is None:
        return

    if isinstance(energy_rate, (float, int)):
        validate_rate(energy_rate)
    elif isinstance(energy_rate, str):
        _validate_rate_profile(ast.literal_eval(energy_rate))
    elif isinstance(energy_rate, dict):
        _validate_rate_profile(energy_rate)
    else:
        raise GSyDeviceException({"misconfiguration": ["energy_rate has an invalid type."]})


def validate_rate(energy_rate):
    """Check that the provided energy rate for Commercial Energy Producer is valid."""
    error_message = {"misconfiguration": [
        "energy_rate should be in between "
        f"{CepSettings.ENERGY_RATE_LIMIT.min} & {CepSettings.ENERGY_RATE_LIMIT.max}."]}
    validate_range_limit(CepSettings.ENERGY_RATE_LIMIT.min, energy_rate,
                         CepSettings.ENERGY_RATE_LIMIT.max, error_message)


def _validate_rate_profile(energy_rate_profile):
    for date, value in energy_rate_profile.items():
        value = float(value)
        error_message = {"misconfiguration": [
            f"energy_rate should at time: {date} be in between "
            f"{CepSettings.ENERGY_RATE_LIMIT.min} & {CepSettings.ENERGY_RATE_LIMIT.max}."]}
        validate_range_limit(CepSettings.ENERGY_RATE_LIMIT.min, value,
                             CepSettings.ENERGY_RATE_LIMIT.max, error_message)
