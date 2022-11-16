# Search looks anywhere inside the string and only returns a match for the first instance
import re

assert re.search(r"world", "Hello world")
assert re.search(r"l", "Hello world").start() == 2


# Match only looks at the start of the string
assert not re.match(r"world", "Hello world")
assert re.match(r"Hello", "Hello world")


# You can ignore case
assert not re.search('hello', 'Hello world')
assert re.search('hello', 'Hello world', re.IGNORECASE)


# Validation example
valid_zip_code = r'[0-9]{5}'
assert re.fullmatch(valid_zip_code, '90210')
assert not re.fullmatch(valid_zip_code, '9021')
assert not re.fullmatch(valid_zip_code, '902100')  # Full match checks that the entire string matches (e.g. no extra characters)
assert not re.fullmatch(valid_zip_code, '9021a')


# Note: \w+ finds all of the words (set of 1 or more alpha characters)
list_of_matches = re.findall(r'\w+', "The quick brown fox jumped over the lazy dog")
print(list_of_matches)


print(re.sub(r'[aeiou]', '_', 'Hello world'))  # Replace with a static string
print(re.sub(r'(\w+)', '~*\\1*~', 'Hello world'))  # Replace with the matched pattern; \\1 refers to what was matched in the ()
