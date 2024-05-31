class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def mark_completed(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def mark_task_completed(self, title):
        current = self.head
        while current:
            if current.task.get_title() == title:
                current.task.mark_completed()
                break
            current = current.next

    def view_todo_list(self):
        current = self.head
        while current:
            task = current.task
            print("Title:", task.get_title())
            print("Description:", task.get_description())
            print("Completed:", task.is_completed())
            print("-----------------------")
            current = current.next


if __name__ == "__main__":
    task1 = Task("Task 1", "Description 1")
    task2 = Task("Task 2", "Description 2")
    task3 = Task("Task 3", "Description 3")

    todo_list = ToDoList()

    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)

    print("Initial ToDoList:")
    todo_list.view_todo_list()

    todo_list.mark_task_completed("Task 2")

    print("\nToDoList after marking Task 2 as completed:")
    todo_list.view_todo_list()
