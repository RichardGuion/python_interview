import pytest


class Solution:
    def isAnagram(self, s, t):
        # this works but it is slow because of the string rebuilding
        if len(s) != len(t):
            return False
        for c in s.lower():
            if c not in t.lower():
                return False
            else:
                pos = t.find(c)
                t = ''.join([t[i] for i in range(len(t)) if i  != pos])
        return True


    def isAnagram2(self, s, t):
        # this works and is acceptable
        # having to sort 2 strings is somewhat expensive
        return sorted(s) == sorted(t)


    def isAnagram3(self, s, t):
        # this works by using 2 maps and comparing the content
        maps = {}
        mapt = {}
        for c in s:
            maps[c] = maps.get(c,0)+1
        for c in t:
            mapt[c] = mapt.get(c,0)+1
        return maps == mapt


@pytest.mark.parametrize("test_string1, test_string2, expected", [
    ('rat', 'tar', True),
    ('rat', 'car', False),
    ("anagram", "nagaram", True),
    ('ccab', 'aacb', False)
])
def testAnagram(test_string1, test_string2, expected):
    sol = Solution()
    assert sol.isAnagram3(test_string1, test_string2) == expected