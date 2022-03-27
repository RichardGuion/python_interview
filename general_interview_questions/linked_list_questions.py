'''
Reverse a singly linked list (as you would use in C++ or Java) in Python
'''

class Node:
    def __init__(self, c, next = None):
        self.val = c
        self.next = next

    def __str__(self):
        return self.val


def list_to_str(head):
    coll = []
    while head is not None:
        coll.append(f'{head}->')
        head = head.next
    coll.append('end.')
    return ''.join(coll)


def print_list(head):
    print(list_to_str(head))


def reverse_list(head):
    # algorithm:
    # the new head points to the previous head - starting out, that is None/Null
    # as we move the head along to the next node, the current item gets moved to the front of the list
    # eventually the head we were given is in the back of the list point to nothing
    # and the new head becomes the former tail
    # Start with list A, B, C, D
    new_head = None
    while head is not None:
        temp = head             # temp = A, then B, then C, then D
        head = head.next        # head = B, then C, then D, then None
        temp.next = new_head    # temp.next = None, then A, then B, then C
        new_head = temp         # new_head = A, then B, then C, then D
    return new_head


def test_reverse_list():
    node4 = Node('D')
    node3 = Node('C', node4)
    node2 = Node('B', node3)
    node1 = Node('A', node2)
    print_list(node1)
    head = reverse_list(node1)
    print_list(head)
    assert list_to_str(head) == 'D->C->B->A->end.'
