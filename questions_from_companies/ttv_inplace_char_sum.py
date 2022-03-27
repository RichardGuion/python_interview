import pytest

'''
given a string like 'aabccccaaa' sum up the frequencies in place
result: 'a2bc4a3***' pad out the remainder of the string with *
perform the operation in place
time should be O(1)
'''

def sum_chars(s):
    char_list = list(s)
    freq = 0
    prev_index  = 0
    prev_char = None
    for index in range(len(char_list)):
        if prev_char == None:
            prev_char = char_list[0]
            freq = 1
        elif prev_char == char_list[index]:
            print(f'prev_char = {prev_char}, freq = {freq}')
            freq += 1
        else:
            print(f'{index} = {char_list[index]}, prev_char = {prev_char}')
            char_list[prev_index] = prev_char
            prev_index += 1
            prev_char = char_list[index]
            if freq > 1:
                char_list[prev_index] = str(freq)
                prev_index += 1
            freq = 1

    # take care of the last char looked at
    char_list[prev_index] = prev_char
    prev_index += 1
    if freq > 1:
        char_list[prev_index] = str(freq)
        prev_index += 1

    # fill in the remainder with *
    for i2 in range(prev_index, len(char_list)):
        char_list[i2] = '*'

    return ''.join(char_list)


@pytest.mark.parametrize("s, expected_output", [
    ('aabccccaaa', 'a2bc4a3***'),
    ('abcd', 'abcd')
])
def test_sum_chars(s, expected_output):
    assert sum_chars(s) == expected_output