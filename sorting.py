from utils import get_frequency


def sort_alphabetically(path, top):
	frequency = get_frequency(path)
	count_in = 0
	count_out = 0
	print('В алфавитном порядке:')
	for k in sorted(frequency.keys()):
		if count_in < top:
			print (k, ': ', frequency[k], sep='')
			count_in += 1
		else:
			count_out += 1


def decreasing_characters_sorting(path, top):
	frequency = get_frequency(path)
	count_in = 0
	count_out = 0
	print("по убыванию длины:")
	sorted_dict = {}
	sorted_keys = sorted(sorted(frequency), key=len, reverse=True) 

	for w in sorted_keys:
		sorted_dict[w] = frequency[w]
	for k in sorted_dict.keys():
		if count_in < top:
			print (k, ': ', sorted_dict[k], sep='')
			count_in += 1
		else:
			count_out += 1

def frequency_of_occurrence_sorting(path, top):
	frequency = get_frequency(path)
	count_in = 0
	count_out = 0
	print("В порядке возрастания частоты:")
	sorted_dict = {}
	sorted_keys = sorted(frequency, key=frequency.get)
	for w in sorted_keys:
		sorted_dict[w] = frequency[w]
	for k in sorted_dict.keys():
		if count_in < top:
			print (k, ': ', sorted_dict[k], sep='')
			count_in += 1
		else:
			count_out += 1
