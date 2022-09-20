def count_lines(name):
	lines: int = 0
	for char in name:
		if "\n" in char:
			lines += 1
	return lines


def count_chars(name: str):
	name = name.replace(' ', "")
	ch = 0
	for _ in name:
		ch += 1
	return ch


def test(name):
	print(f"There are {count_lines(name)} lines and {count_chars(name)} chars.")
