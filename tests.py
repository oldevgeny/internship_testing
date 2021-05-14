# pip install pytest
import pytest
from validators import validate_output_order, validate_top, validate_path



@pytest.mark.parametrize("text, expected_result",  [('1', 1),
													('2', 2),
													('3', 3),
													('4', None),
													('0', None),
													('dsadsa', None),
													('21ds', None),
													('123', None),
													('dsa1321', None),
													(1, 1),
													(2, 2),
													(3, 3),
													])
def test_validate_output_order(text, expected_result):
	orig_validate_output_order = validate_output_order.__wrapped__
	assert orig_validate_output_order(text) == expected_result




@pytest.mark.parametrize("text, expected_result",  [('1', 1),
													('2', 2),
													('3', 3),
													('4', 4),
													('0', None),
													('dsadsa', None),
													('21ds', None),
													('123', 123),
													('dsa1321', None),
													(1, 1),
													(2, 2),
													(3, 3),
													(1000, 1000),
													])
def test_validate_top(text, expected_result):
	orig_validate_top = validate_top.__wrapped__
	assert orig_validate_top(text) == expected_result



@pytest.mark.parametrize("text, expected_result",  [('4', None),
													('0', None),
													('dsadsa', None),
													('21ds', None),
													('123', None),
													('dsa1321', None),
													('dadsa.txt', None),
													('input.txt', 'input.txt')
													])
def test_validate_path(text, expected_result):
	orig_validate_path = validate_path.__wrapped__
	assert orig_validate_path(text) == expected_result
