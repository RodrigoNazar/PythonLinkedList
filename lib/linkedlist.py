
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'''{self.val}'''


class LinkedList:
    def __init__(self, head_val):
        self.head = Node(head_val)
        self.len = 1

    def append(self, val):
        tail = self.head
        while tail:
            pnode = tail  # previous node
            tail = tail.next
        tail = Node(val)
        pnode.next = tail
        self.len += 1

    def remove(self, elem):
        indx = 1
        node = self.head

        while indx <= self.len:
            if node.val == elem:
                # We found it
                break
            indx += 1
            pnode = node  # previous node
            node = node.next

        if indx == 1:
            # We change the head
            aux = node.next
            del self.head
            self.head = aux
            self.len -= 1

        elif indx == self.len:
            # We change the tail
            del node
            pnode.next = None
            self.len -= 1

        elif node is None:
            # We did not found the element
            raise ValueError('linkedlist.remove(x): x not in linkedlist')

        else:
            # The node is in the middle
            pnode.next = node.next
            del node
            self.len -= 1

    def __iter__(self):
        self.cursor = self.head
        return self

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        current = self.cursor
        self.cursor = self.cursor.next
        return current

    def __len__(self):
        return self.len

    def __repr__(self):
        node = self.head
        rep = ''
        while node:
            rep += ' ' + str(node) + ' ->'
            node = node.next
        rep = rep[1:-3]
        return rep
