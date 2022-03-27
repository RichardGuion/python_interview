'''
  Some experiments with string
'''
class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()

s = 'this is how the world will end, one day the world ends in fire'

# split a string into a list of tokens
list_words = s.split()
print(f'complete string split into list of words: {list_words}')
print(f'unique words in above string: {list(set(list_words))}')

# reverse a sentence by first reversing a list then joining it as a string
print (' '.join(list_words[::-1]))

# examples of slicing a string
example = 'A string that we will slice up.'
print(f'0 to 10 slice: {example[:10]}')
print(f'10 to 20 slice: {example[10:20]}')
print(f'20 to the end slice: {example[20:]}')

