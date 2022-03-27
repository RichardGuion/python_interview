'''
  An example of a stack class in python
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items ) -1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push('d')
stack.push('c')
stack.push('b')
stack.push('a')

print(f'peek = {stack.peek()}')
print(f'size = {stack.size()}')
print(f'isEmpty = {stack.isEmpty()}')

for index in range(0, stack.size()):
    item = stack.pop()
    print(f'item popped = {item}')
