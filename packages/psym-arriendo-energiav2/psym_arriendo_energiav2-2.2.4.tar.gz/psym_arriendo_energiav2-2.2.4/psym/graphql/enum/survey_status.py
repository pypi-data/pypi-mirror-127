#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from enum import Enum


class SurveyStatus(Enum):
    PLANNED = "PLANNED"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    MISSING_ENUM = ""

    @classmethod
    def _missing_(cls, value: object) -> "SurveyStatus":
        return cls.MISSING_ENUM
