import functools
import re


def valid_helper(func):
    @functools.wraps(func)
    def wrapped(text):
        arg = None
        while arg == None:
            arg = func(input(text))
        return arg
    return wrapped

def get_frequency(path):
	frequency = {}
	with open(path) as f:
		text_string = f.read().lower()
		match_pattern = re.findall(r'\b[а-яё]+|[a-z]{1,100}\b', text_string)
		for word in match_pattern:
			fr_count = frequency.get(word,0)
			frequency[word] = fr_count + 1

		return frequency
