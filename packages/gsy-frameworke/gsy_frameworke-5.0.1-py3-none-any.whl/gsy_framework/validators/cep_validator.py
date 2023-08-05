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
from gsy_framework.validators.base_validator import BaseValidator
from gsy_framework.validators import utils


class CommercialProducerValidator(BaseValidator):
    """Validator class for Commercial Producers."""

    @classmethod
    def validate(cls, **kwargs):
        """Validate the parameters of the device."""
        utils.validate_energy_rate(**kwargs)
