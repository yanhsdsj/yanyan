#4 链表增删改查工作
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    #链表
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next #向后移动一个指针
            current.next = new_node
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next:
                    current = current.next
                else:
                    raise IndexError("Invalid position")
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next:
                    current = current.next #到position为止
                else:
                    raise IndexError("Invalid position") #索引不正常
            if current.next is None:
                raise IndexError("Invalid position")
            current.next = current.next.next #删除current.next

    def search(self, data):
        current = self.head
        while current: #向后轮替
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
