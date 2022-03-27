'''
Write code to decode strings.
For example,
String str = "3[a2[bd]g4[ef]h]",
the output should be "abdbdgefefefefhabdbdgefefefefhabdbdgefefefefh".
'''
import pytest

def decodeString(encStr):
    string_tokens = []
    current_token = ''
    for index in reversed(range(len(encStr))):
        if encStr[index] == ']':
            if len(current_token) > 0:
                string_tokens.insert(0, current_token)
            current_token = ''
            print(f'current token cleared, list = {string_tokens}')
        elif encStr[index] == '[':
            print('closing bracket found')
        elif encStr[index].isdigit():
            current_token = current_token * int(encStr[index])
            print(f'String repeated = {current_token}')
            if index < len(encStr)-1 and encStr[index+1] == '[':
                if len(string_tokens) > 0:
                    last_token = string_tokens[0]
                    del string_tokens[0]
                    current_token = ''.join([current_token, last_token])
                    print(f'token popped and joined, new token is {current_token}')
        else:
            current_token = encStr[index] + current_token
            print(f'current token now is {current_token}')
    return current_token


@pytest.mark.parametrize("encStr, expected", [
    ('3[a2[bd]g4[ef]h]', 'abdbdgefefefefhabdbdgefefefefhabdbdgefefefefh')
])
def testDecodeString(encStr, expected):
    assert(decodeString(encStr)) == expected