class Queue:
    def __init__(self):
        self.data = []
        self.tail = -1
        self.max_size = 15

    def enqueue(self, newData):
        if (self.tail == self.max_size - 1):
            print("Can't insert into a full queue")
        else:
            self.data.append(newData)
            print("Enqueue the data: " + str(newData))
            print("Data enqueued: " + "\nNew list: " + str(self.data))
    
    def dequeue(self):
        if not self.data:
            print("Cannot dequeue from empty list")
        else:
            self.data.pop(0)
            print("Dequeuing data..." + "\nNew list: " + str(self.data))
            

    def peek(self):
        print("Item at head of list: " + str(self.data[0]))

    def length(self):
        print("Length of list: " + str(len(self.data)))

class Stack:
 def __init__(self):
   self.index = []

 def __len__(self):
   return len(self.index)

 def push(self,item):
   self.index.insert(0,item)

 def peek(self):
   if len(self) == 0:
     raise Exception("peek() called on empty stack.")
   return self.index[0]

 def pop(self):
   if len(self) == 0:
     raise Exception("pop() called on empty stack.")
   return self.index.pop(0)

class Reverse:
    def __init__(self):
      self.stack = []
      self.maxSize = 100
    
    def reverse(self):
        newStack = Stack()
        if not self.stack:
         print("Reverse() called on empty stack.")
        
        else:
            while not self.stack.is_empty():
               newStack.push(self.stack.pop())
            self.stack = newStack