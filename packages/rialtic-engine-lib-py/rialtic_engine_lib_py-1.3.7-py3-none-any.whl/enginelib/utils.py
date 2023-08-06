import enum
import json

from fhir.resources.fhirtypes import Date
from testcases.testcase import InsightEngineTestCase
from enginelib.claim_focus import ClaimFocus

class _DateUnit(enum.Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


def test_case_from_file(filename: str) -> InsightEngineTestCase:
    with open(filename) as test_case_file:
        test_case_obj = json.load(test_case_file)
        return InsightEngineTestCase.parse_obj(test_case_obj)


def claim_focus_from_test_case(path: str) -> ClaimFocus:
    tc = test_case_from_file(path)
    return ClaimFocus(tc.insight_engine_request.claim,
                      tc.insight_engine_request)


def date_diff(first: Date, second: Date, unit: str) -> int:
    """
    :param unit: one of supported date units: day, month, year
    """
    # No exception handling, because enum exception is fine.
    date_unit = _DateUnit(unit)
    if date_unit == _DateUnit.DAY:
        diff = (first - second).days
    elif date_unit == _DateUnit.MONTH:
        diff = (
            (first.year - second.year) * 12
            + (first.month - second.month)
            - (first.day < second.day)
        )
    elif date_unit == _DateUnit.YEAR:
        diff = (
            first.year
            - second.year
            - ((first.month, first.day) < (second.month, second.day))
        )
    else:
        raise ValueError(f"{unit} unit is not supported")
    return diff
