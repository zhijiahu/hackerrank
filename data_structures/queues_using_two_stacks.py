
"""
1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
"""
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        return self.stack1[0]
        
    def pop(self):
        del self.stack1[0]
        return self.stack2.pop()
        
    def put(self, value):
        self.stack1.append(value)

        temp = list(self.stack1)

        while len(temp) > 0:
            self.stack2.append(temp.pop())


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
