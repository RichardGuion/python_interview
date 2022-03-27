import pytest

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    rev_list = []
    for index in range(len(s))[::-1]:
        rev_list.append(s[index])
    return ''.join(rev_list)


def reverseString2(s):
    """
    :type s: str
    :rtype: str
    """
    rev_list = list(s)
    for index in range(len(s)//2):
        char = rev_list[index]
        rev_list[index] = rev_list[len(s) - (index+1)]
        rev_list[len(s) - (index + 1)] = char
    return ''.join(rev_list)


def reverseString3(s):
    """
    :type s: str
    :rtype: str
    """
    rev_list = list(s)
    forward_index, back_index = 0, len(s) - 1
    while forward_index < back_index:
        rev_list[forward_index], rev_list[back_index] = rev_list[back_index], rev_list[forward_index]
        forward_index += 1
        back_index -= 1
    return ''.join(rev_list)


def reverseStringRecursive(s):
    l = len(s)
    if l < 2:
        return s
    return reverseStringRecursive(s[l // 2:]) + reverseStringRecursive(s[:l // 2])


@pytest.mark.parametrize("s, expected_output", [
    ('hello', 'olleh'),
])
def test_reverse_string(s, expected_output):
    assert reverseString(s) == expected_output


@pytest.mark.parametrize("s, expected_output", [
    ('hello', 'olleh'),
    ('sand', 'dnas'),
    ('thisisus', 'susisiht')
])
def test_reverse_string2(s, expected_output):
    assert reverseString2(s) == expected_output


@pytest.mark.parametrize("s, expected_output", [
    ('hello', 'olleh'),
    ('thisisus', 'susisiht')
])
def test_reverse_string3(s, expected_output):
    assert reverseString3(s) == expected_output


@pytest.mark.parametrize("s, expected_output", [
    ('hello', 'olleh'),
    ('thisisus', 'susisiht')
])
def test_reverse_string_recursive(s, expected_output):
    assert reverseStringRecursive(s) == expected_output
