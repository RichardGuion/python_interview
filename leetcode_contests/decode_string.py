import pytest
import re

'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
'''

def decodeAtIndex(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    # this regex findall will return a list of tuples, alphanumeric & digit
    # [(a, 23)]
    # [(leet, 2), (code, 3)]
    items = re.findall(r'(\w+?)(\d+)', S)
    if len(items) == 0:
        return S[K-1]

    # if len(items) == 1:
    #     item_str, freq = items[0]
    #     freq = int(freq[::-1])
    #     print(f'item_str = {item_str} freq = {freq}')
    #     total = 0
    #     while freq > 0:
    #         total += freq % 10
    #         print(f'total is {total}')
    #         freq = freq // 10
    #     if K-1 <= total:
    #         return item_str[K-1]
    #     else:
    #         return None

    print(items)
    decodedString = ''
    for item in items:
        print(item)
        item_str, freq = item
        decodedString += item_str
        freq = int(freq[::-1])
        print(f'item_str = {item_str} freq = {freq}')
        while freq > 0:
            freq_digit = freq % 10
            print(f'freq_digit is {freq_digit}')
            decodedString = decodedString * freq_digit
            freq = freq // 10
            if len(decodedString) >= K:
                break
            print(f'len of decodedString = {len(decodedString)}')
    print(decodedString)
    return decodedString[K-1]

    # print(items)
    # decodedString = ''
    # for item in items:
    #     print(item)
    #     item_str, freq = item
    #     freq = int(freq[::-1])
    #     print(f'item_str = {item_str} freq = {freq}')
    #     item_chunk = decodedString + item_str
    #     print(f'item_chunk = {item_chunk}')
    #     decodedString = ''
    #     while freq > 0:
    #         freq_range = freq % 10
    #         print(f'freq_range is {freq_range}')
    #         for i in range(freq_range):
    #             decodedString += item_chunk
    #             print(f'in loop = {decodedString}')
    #         freq = freq // 10
    #         item_chunk = decodedString
    # print(f'len of decodedString = {len(decodedString)}')
    # print(decodedString)
    # return decodedString[K-1]

# leet2code3
# expected: "leetleetcodeleetleetcodeleetleetcode"
# actual:   "leetleetcodeleetleetcodeleetleetcode"

# ha22
# expected: "hahahaha"

# a2345678999999999999999
# expected: The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


def decodeAtIndex2(S, K):
    N = 0
    for i, c in enumerate(S):
        N = N * int(c) if c.isdigit() else N + 1
        if K <= N: break
    for j in range(i, -1, -1):
        c = S[j]
        if c.isdigit():
            N /= int(c)
            K %= N
        else:
            if K == N or K == 0: return c
            N -= 1


@pytest.mark.parametrize("S, K, expected", [\
    ('a23', 6, 'a'),
    ('abc', 1, 'a'),
    ('leet2code3', 10, 'o'),
    ('ha22', 5, 'h'),
    ('a2345678999999999999999', 1, 'a'),
    # causes memory overflow
    ("y959q969u3hb22odq595", 222280369, 'h')
])
def test_decode(S, K, expected):
    assert decodeAtIndex2(S, K) == expected
