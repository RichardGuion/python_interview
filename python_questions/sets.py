'''
  sets are powerful tools in python
  sets contain unique items
  they are immutable and faster at searching than lists
  one drawback is that sets return items in a random order
'''
# find words in sent1 and in sent2
def find_same_words(sent1, sent2):
    set1 = set(sent1.split())
    set2 = set(sent2.split())
    print(set1 & set2)

# find letters in sent1 not in sent2
def find_sent1_letters(sent1, sent2):
    set1 = set(sent1)
    set2 = set(sent2)
    print(set1 - set2)

# find letters in both sent1 and sent2
def find_same_letters(sent1, sent2):
    set1 = set(sent1)
    set2 = set(sent2)
    print(set1 & set2)

# find letters that are not in both sent
def find_letters_in_either_not_both(sent1, sent2):
    set1 = set(sent1)
    set2 = set(sent2)
    print(set1 ^ set2)

find_same_words('How now brown cow', "The cow went to the moon")
find_sent1_letters('How now brown cow', "The cow went to the moon")
find_same_letters('How now brown cow', "The cow went to the moon")
find_letters_in_either_not_both('How now brown cow', "The cow went to the moon")
