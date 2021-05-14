# pip install pytest
import pytest
from validators import validate_output_order

# @pytest.mark.parametrize()
def test_validate_output_order():
	assert validate_output_order('2') == 2
