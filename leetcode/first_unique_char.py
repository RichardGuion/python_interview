import pytest
from collections import OrderedDict

def firstUniqChar(s):
    freq = OrderedDict()
    for char in s:
        freq[char] = 1 if char not in freq else freq[char] + 1
    print(freq)
    for k,v in freq.items():
        if v == 1:
            return s.find(k)
    return -1


@pytest.mark.parametrize("s, expected", [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('', -1)
])
def test_unique_char(s, expected):
    assert firstUniqChar(s) == expected