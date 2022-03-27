import pytest
from collections import OrderedDict

def firstUniqChar(s):
    freq = OrderedDict()
    for char in s:
        if s.isdigit():
            freq[char] = 1 if char not in freq else freq[char] + 1
    print(freq)
    for k,v in freq.items():
        if v == 1:
            return int(k)


@pytest.mark.parametrize("s, expected", [
    ('2124014', 0),
    ('2332123423523454322241543597', 9)
])
def test_unique_char(s, expected):
    assert firstUniqChar(s) == expected