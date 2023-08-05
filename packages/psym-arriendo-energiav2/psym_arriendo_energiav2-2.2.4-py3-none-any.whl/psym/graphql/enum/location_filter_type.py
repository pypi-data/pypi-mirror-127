#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from enum import Enum


class LocationFilterType(Enum):
    LOCATION_INST = "LOCATION_INST"
    LOCATION_INST_NAME = "LOCATION_INST_NAME"
    LOCATION_INST_EXTERNAL_ID = "LOCATION_INST_EXTERNAL_ID"
    LOCATION_TYPE = "LOCATION_TYPE"
    LOCATION_INST_HAS_EQUIPMENT = "LOCATION_INST_HAS_EQUIPMENT"
    PROPERTY = "PROPERTY"
    MISSING_ENUM = ""

    @classmethod
    def _missing_(cls, value: object) -> "LocationFilterType":
        return cls.MISSING_ENUM
