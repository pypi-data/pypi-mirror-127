#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from enum import Enum


class FlowNewInstancesPolicy(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    MISSING_ENUM = ""

    @classmethod
    def _missing_(cls, value: object) -> "FlowNewInstancesPolicy":
        return cls.MISSING_ENUM
