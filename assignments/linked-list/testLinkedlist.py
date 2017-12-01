# mylist = LinkedList()
#
# mylist.append('a')
# mylist.append('b')
# mylist.append('c')
#
# print(mylist.head.data)  # => 'a'
# print(mylist.tail.data)  # => 'c'
# print(mylist.find(lambda data: data > 'b'))  # => 'c'
# print(mylist.delete('a'))
# print(mylist.head.data)  # => 'b'

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next  = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def extractor(self, index):
        if index >= self.length():
            print(ValueError)
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: return cur_node.data
            cur_index += 1

    def delete(self, index):
        if index >= self.length():
            print(ValueError)
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

myList = LinkedList()

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
myList.append(6)

myList.display()

print("Element at 2nd index: %d" % myList.extractor(5))

myList.delete(1)
myList.display()
print(myList.length())
