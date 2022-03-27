import pytest

'''
   Problem: Find words in a sentence that have a frequency greater than 1
            Ignore punctuation and case
'''

def find_duplicate_words(sentence):
    # make string lowercase
    x = sentence.lower()
    # strip punctuation
    import string
    f = ''.join([i for i in x if i not in string.punctuation])
    from collections import defaultdict
    freq = defaultdict(int)
    for word in f.split():
        freq[word] += 1
    coll = []
    for k,v in freq.items():
        if v > 1:
            coll.append((k, v))
    return coll


@pytest.mark.parametrize('sentence, expected_word_freq', [
    ('The cow was brown, and then it went to town.', []),
    ('This is how The World will end, one day the world ends in fire', [('the', 2), ('world', 2)])
])
def test_duplicate_words(sentence, expected_word_freq):
    assert find_duplicate_words(sentence) == expected_word_freq
