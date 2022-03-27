import pytest

'''
  Problem: given a string, and a letter to search for within the string,
  return all indexes that contain the letter
'''

# Complete the characterSearch function below.
def characterSearch(word, letter):
    indexes = []
    for index in range(len(word)):
        if word[index] == letter:
            indexes.append(index)
    return indexes


@pytest.mark.parametrize('word, letter, expected', [
    ('Bitgo is amazing', 'i', [1, 6, 13]),
    ('apple', 'z', [])
])
def test_char_search(word, letter, expected):
    assert characterSearch(word, letter) == expected