class Stack:
    def __init__(self, size):
        self.size = size
        self.elements = [0] * size
        self.top_index = 0

    def stack_empty(self):
        return self.top_index == 0

    def push_element(self, x):
        if self.top_index == self.size:
            print("Stack overflow")
        else:
            self.elements[self.top_index] = x
            self.top_index += 1

    def pop_element(self):
        if self.top_index == 0:
            print("Stack underflow")
        else:
            self.top_index -= 1
            return self.elements[self.top_index]


class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue overflow")
        else:
            self.queue[self.rear] = x
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.front == self.rear:
            print("Queue underflow")
        else:
            x = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return x


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.nil = Node(None)

    def list_search(self, k):
        x = self.nil.next
        while x is not None and x.data != k:
            x = x.next
        return x

    def list_insert(self, x):
        x.next = self.nil.next
        self.nil.next = x

    def list_delete(self, x):
        if x.next is not None:
            x.next = x.next.next
        else:
            # If x is the last node, we need to update the nil's next pointer
            prev = self.nil
            while prev.next != x:
                prev = prev.next
            prev.next = None


if __name__ == "__main__":
   
    # Stack
    elements = Stack(5)
    print("Is Stack empty: ", elements.stack_empty())
    elements.push_element(3)
    elements.push_element(6)
    elements.push_element(5)
    print("Is Stack empty:", elements.stack_empty())
    print("Elements popped from stack: ", elements.pop_element())
    print("Elements popped from stack: ", elements.pop_element())
    print("Is Stack empty: ", elements.stack_empty())

    # Queue
    queue = Queue(5)
    print("Is Queue empty: ", queue.front == queue.rear)
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    print("Is Queue empty: ", queue.front == queue.rear)
    print("Dequeued from queue: ", queue.dequeue())
    print("Dequeued from queue: ", queue.dequeue())
    print("Is Queue empty: ", queue.front == queue.rear)

    #linked list
    linked_list = SinglyLinkedList()
    print("Element in list(10): ", linked_list.list_search(10))
    node1 = Node(10)
    linked_list.list_insert(node1)
    print("Element in list(10): ", linked_list.list_search(10).data)
    node2 = Node(50)
    linked_list.list_insert(node2)
    linked_list.list_delete(node1)
    print("Element in list(10): ", linked_list.list_search(10))
    print("Element in list(50): ", linked_list.list_search(50).data)
