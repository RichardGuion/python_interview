
'''
   Problem: take a string, ignore punctuation, ignore case and print the frequency of words
   in sorted descending order of frequency
'''
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
    for k,v in sorted(freq.items(), key=itemgetter(1), reverse=True):
        print(f'word: {k} freq: {v}')


freq_count('The cow was brown, and then it went to town.')
freq_count('this is how the world will end, one day the world ends in fire')

