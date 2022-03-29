'''
   Problem: take a string, ignore punctuation, ignore case and print the frequency of words
   in sorted descending order of frequency
'''
import pytest


def freq_count(sentence):
    # make string lowercase
    x = sentence.lower()
    # strip punctuation
    import string
    f = ''.join([i for i in x if i not in string.punctuation])
    # default dict assumes default value is 0 if not found.
    from collections import defaultdict
    freq = defaultdict(int)
    for word in f.split():
        freq[word] += 1
    # sort the dict in reverse order by the value item
    from operator import itemgetter
    coll = []
    for k, v in sorted(freq.items(), key=itemgetter(1), reverse=True):
        coll.append((k, v))
        # print(f'word: {k} freq: {v}')
    return coll


@pytest.mark.parametrize('sentence, expected_word_freq', [
    ('hey now', [('hey', 1), ('now', 1)]),
    ('Hey hey HEY', [('hey', 3)]),
    ('Hey hey HEYzzzz', [('hey', 2), ('heyzzzz', 1)]),
    ('The cow was brown, and then it went to town.',
     [('the', 1), ('cow', 1), ('was', 1), ('brown', 1), ('and', 1), ('then', 1), ('it', 1), ('went', 1), ('to', 1),
      ('town', 1)]),
    ('This is how The World will end, one day the world ends in fire',
     [('the', 2), ('world', 2), ('this', 1), ('is', 1), ('how', 1), ('will', 1), ('end', 1), ('one', 1), ('day', 1),
      ('ends', 1), ('in', 1), ('fire', 1)])
])
def test_freq_count(sentence, expected_word_freq):
    assert (freq_count(sentence) == expected_word_freq)
