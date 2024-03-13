import json

import pytest

from lodash_python.main import Method, calculations, ceil

calculation_params = [
    {"method": Method.ADD.value, "first": 1, "second": 2, "expected_result": 3},
    {"method": Method.ADD.value, "first": 10, "second": 23, "expected_result": 33},
    {"method": Method.SUBTRACT.value, "first": 100, "second": 25, "expected_result": 75},
    {"method": Method.SUBTRACT.value, "first": 10, "second": 25, "expected_result": -15},
    {"method": Method.MULTIPLY.value, "first": 10, "second": 25, "expected_result": 250},
    {"method": Method.MULTIPLY.value, "first": 0, "second": 25, "expected_result": 0},
    {"method": Method.DIVIDE.value, "first": 10, "second": 5, "expected_result": 2},
    {"method": Method.DIVIDE.value, "first": 0, "second": 5, "expected_result": 0},
]


@pytest.mark.parametrize('params', calculation_params)
def test_calculations(params: json):
    json_dump = json.dumps(params)
    json_param = json.loads(json_dump)

    add_result = calculations(json_param["method"], json_param["first"], json_param["second"])
    assert add_result == json_param["expected_result"]


def test_ceil():
    ceil_result = ceil(1.2)
    expected_result = 2
    assert ceil_result == expected_result
