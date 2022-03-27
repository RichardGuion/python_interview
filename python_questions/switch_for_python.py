'''
  Python has no built in switch statement, unlike Java or C++
  I found this example of a method which returns a value using a dictionary
  Almost like a switch statement!
'''
def f(x):
    return {
        1 : 'output for case 1',
        2 : 'output for case 2',
        3 : 'output for case 3'
    }.get(x, 'default case')

print(f(2))
