import pytest

'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''

# this method works in a regular fashion and more like how I would do it in C++
# going to the last character in the string and adding it, while multiplying the digit
# by a power of 10
# however the test cases they have with alphas in the middle of a number string
# the second case works best
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    ret_val = 0
    # strip leading white spaces
    str = str.strip()

    # this double sign combo is invalid
    if '+-' in str or '-+' in str:
        return 0

    # starting off with alpha is invalid
    if len(str) > 0 and str[0].isalpha():
        return 0

    power_index = 0
    for char in reversed(str):
        if char.isdigit():
            digit = int(char) * (10 ** power_index)
            ret_val += digit
            power_index += 1
        elif char == '-':
            # negative sign found
            ret_val = ret_val * -1
        elif char == '+':
            continue
        else:
            # alpha in middle of number, forget everything to the right
            ret_val = 0
            power_index = 0

    return max(min(ret_val, 2147483647), -2147483648)


# go forward and stop at the first non numeric character
# use the built in int function to transform from int to string
def myAtoi2(str):
    s = str.strip()

    i = s[:1] in "+-"
    while i < len(s) and s[i] in "0123456789": i += 1
    substr = s[:i]

    result = 0 if not substr or substr in "+-" else int(substr)
    return max(min(result, 2147483647), -2147483648)


@pytest.mark.parametrize("input_str, expected", [
    ('42', 42),
    ('   -42', -42),
    ('4193 with words', 4193),
    ('words and 987', 0),
    ('-91283472332', -2147483648),
    ('3.14159', 3),
    ('+-2', 0),
    ('-+1', 0),
    ('  -0012a42', -12),
    ('+1', 1),
    ('2147483648', 2147483647),
    ('0-1', 0)
])
def test_atoi(input_str, expected):
    assert(myAtoi2(input_str) == expected)