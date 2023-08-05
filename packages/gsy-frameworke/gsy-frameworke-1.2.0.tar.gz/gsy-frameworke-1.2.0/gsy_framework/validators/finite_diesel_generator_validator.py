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
from gsy_framework.constants_limits import ConstSettings
from gsy_framework.exceptions import GSyDeviceException
from gsy_framework.validators import utils
from gsy_framework.validators.cep_validator import CommercialProducerValidator

CepSettings = ConstSettings.CommercialProducerSettings


class FiniteDieselGeneratorValidator(CommercialProducerValidator):
    """Validator class for Finite Diesel Generators."""

    @classmethod
    def validate(cls, **kwargs):
        """Validate the parameters of the device."""
        if kwargs.get("max_available_power_kW") is not None:
            if isinstance(kwargs["max_available_power_kW"], (int, float)):
                error_message = {
                    "misconfiguration": ["max_available_power_kW should be in between "
                                         f"{CepSettings.MAX_POWER_KW_LIMIT.min} & "
                                         f"{CepSettings.MAX_POWER_KW_LIMIT.max}."]}
                utils.validate_range_limit(
                    CepSettings.MAX_POWER_KW_LIMIT.min,
                    kwargs["max_available_power_kW"],
                    CepSettings.MAX_POWER_KW_LIMIT.max,
                    error_message)
            elif isinstance(kwargs["max_available_power_kW"], dict):
                error_message = {
                    "misconfiguration": ["max_available_power_kW should be in between "
                                         f"{CepSettings.MAX_POWER_KW_LIMIT.min} & "
                                         f"{CepSettings.MAX_POWER_KW_LIMIT.max}."]}
                for value in kwargs["max_available_power_kW"].values():
                    utils.validate_range_limit(
                        CepSettings.MAX_POWER_KW_LIMIT.min, value,
                        CepSettings.MAX_POWER_KW_LIMIT.max, error_message)
            else:
                raise GSyDeviceException({
                    "misconfiguration": ["max_available_power_kW has an invalid type."]})

        super().validate(**kwargs)
