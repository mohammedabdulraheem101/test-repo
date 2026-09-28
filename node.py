class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> " if current.next is not None else "")
            current = current.next
        print()

    def search(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                print(f"data is at {index} found")
                return True
            current = current.next
            index += 1
        print("data is not found")
        return False

    def delete(self, data):
        current = self.head
        previous = None

        if self.head is None:
            return False

        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def length(self):
        print(self.size)

    def insertatbeg(self, data):
        obj = Node(data)
        obj.next = self.head
        self.head = obj
        self.size += 1
        self.traverse()

    def deletelast(self):
        if self.head is None:
            return False

        if self.head.next is None:
            self.head = None
            self.size = 0
            self.traverse()
            return True

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None
        self.size -= 1
        self.traverse()
        return True


ll = linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traverse()
ll.search(10)
ll.delete(10)
ll.length()
ll.insertatbeg(90)
ll.deletelast()