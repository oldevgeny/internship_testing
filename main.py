# pip install pathvalidate
from pathvalidate import ValidationError, validate_filename

import os
from pathlib import Path

from validators import validate_output_order, validate_top, validate_path
from validators import t_1, t_2, t_3
from sorting import sort_alphabetically
from sorting import decreasing_characters_sorting
from sorting import frequency_of_occurrence_sorting

def main():
	base_path = Path(__file__).resolve().parent
	path = os.path.join(base_path, validate_path(t_3))
	output_order = validate_output_order(t_1)
	top = validate_top(t_2)

	if output_order == 1:
		decreasing_characters_sorting(path, top)
	elif output_order == 2:
		frequency_of_occurrence_sorting(path, top)
	elif output_order == 3:
		sort_alphabetically(path, top)


if __name__ == '__main__':
    main()
