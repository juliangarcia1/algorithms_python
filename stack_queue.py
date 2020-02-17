class Stack:
    def __init__(self):
        self.top = 0
        self.x = [0] * 10

    def push(self, val):
        self.top += 1
        self.x[self.top] = val
        self.print_info()

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        self.top -= 1
        return self.x[self.top + 1]

    def is_empty(self):
        if self.top == 0:
            return True
        return False

    def print_info(self):
        print(f'\tStack:{self.x}: Top{self.top}')


class Queue:
    def __init__(self):
        self.head = 0
        self.tail = 0
        pass

    def enqueue(self):
        pass

    def dequeue(self):
        pass


st = Stack()
st.print_info()
st.push(1)
st.push(3)
st.push(5)
st.push(6)
st.print_info()
st.pop()
st.print_info()
