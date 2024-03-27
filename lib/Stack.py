class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit


    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack overflow: cannot push item, stack is full.")    

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack underflow: cannot pop item, stack is empty")
            return None 

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None    
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            index = self.items.index(target)
            return self.size() - index - 1
        except ValueError:
            return -1      #search functions return -1 when the target item is not found 

stk = Stack([5,6,7,8,9,10])
