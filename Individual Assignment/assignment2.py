class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if position == 1:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def delete_after_node(self, node):
        if node is None or node.next is None:
            print("Node does not exist or is the last node")
            return
        node_to_delete = node.next
        node.next = node.next.next
        node_to_delete.next = None

    def search_node(self, value):
        current = self.head
        position = 1
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return
        return self.head.data


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_pos(5, 1)
    linked_list.insert_at_pos(10, 2)
    linked_list.insert_at_pos(15, 3)
    linked_list.insert_at_pos(20, 2)
    print("LinkedList after insertion:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.delete_at_position(3)
    print("LinkedList after deletion at position 3:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    node_to_delete_after = linked_list.head
    linked_list.delete_after_node(node_to_delete_after)
    print("LinkedList after deleting node after first node:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("Position of value 10:", linked_list.search_node(10))
    print("Position of value 25:", linked_list.search_node(25))

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Peek after pop:", stack.peek())
