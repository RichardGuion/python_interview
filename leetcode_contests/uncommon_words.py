import pytest
from collections import OrderedDict

'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

'''


def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    dict_words = OrderedDict()
    for word in A.split():
        dict_words[word] = 1 if word not in dict_words else dict_words[word] + 1
    for word in B.split():
        dict_words[word] = 1 if word not in dict_words else dict_words[word] + 1

    list_uncommon = []
    for k,v in dict_words.items():
        if v == 1:
            list_uncommon.append(k)
    return list_uncommon


@pytest.mark.parametrize('sent1, sent2, expected', [
    ('this apple is sweet', 'this apple is sour', ['sweet','sour']),
    ('apple apple', 'banana', ['banana'])
])
def test_uncommon(sent1, sent2, expected):
    assert uncommonFromSentences(sent1, sent2) == expected