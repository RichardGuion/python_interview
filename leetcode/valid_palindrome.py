import re

import pytest


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # s = ''.join(s.split())
    regex = re.compile('[^0-9a-zA-Z]')
    s = regex.sub('', s.lower())
    last_string_pos = len(s) - 1
    for index in range(len(s) // 2):
        if s[index] != s[last_string_pos - index]:
            return False
    return True


@pytest.mark.parametrize("test_string, expected", [
    ('0P', False),
    ('kayak', True),
    ('racecar', True),
    ('Noon', True),
    ('Nothing', False),
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False)
])
def test_palindrome(test_string, expected):
    assert isPalindrome(test_string) == expected

