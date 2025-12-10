class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def begin(self,data):
           new_node = Node(data)
           new_node.next = self.head
           self.head = new_node
    def ending(self,data):
        new_node = Node(data)
        # if self.head is None:  # If train is empty
        #     self.head = new_node
        #     return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
    def printf(self):
        current = self.head
        while(current):
            print(current.data , end = " -> ")
            current = current.next
        print("None")
print("Running")
l1 = linked()
l1.begin(5)
l1.begin(7)
l1.ending(97779)
l1.begin(15)
l1.ending(999)
l1.begin(73)
l1.printf()

