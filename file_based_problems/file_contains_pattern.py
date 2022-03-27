import pytest

'''
   Problem: given a text file where a string like Hello World can appear in the middle of text
            or even broken up by a new line, find the string in the file 
'''

# Approach 1: Reading a file 1 byte at a time and comparing against the pattern.
def file_contains(filepath, pattern):
    file = open(filepath, 'r')
    read_size = 1
    read_buffer = file.read(read_size)
    while read_buffer:
        pattern_index = 0
        while pattern_index < len(pattern) and read_buffer == pattern[pattern_index]:
            pattern_index += 1
            read_buffer = file.read(read_size)

        if pattern_index >= len(pattern):
            return True
        read_buffer = file.read(read_size)
    return False


@pytest.mark.parametrize('filepath, pattern, expected', [
    ('./test_data/test_file.txt', 'hello world', True),
    ('./test_data/test_file2.txt', 'hello world', True),
    ('./test_data/test_file3.txt', 'hello\nworld', True),
    ('./test_data/test_file4.txt', 'hello\nworld', False),
])
def test_file_contains(filepath, pattern, expected):
    assert file_contains(filepath, pattern) == expected