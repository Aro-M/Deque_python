class Deque:
    def __init__(self):
        self.value  = []
    def __add__(self, other):
        return Deque(self.value + self.other.value)
    def addFront(self,val):
        return self.value.append(val)
    def addEnd(self,val):
        return self.value.insert(len(self.value),val)
    def removeFront(self):
        return  self.value.pop(0)
    def removeEnd(self):
        return  self.value.pop(-1)
    def size_Deq(self):
        return len(self.value)
    def isEmpty(self):
        if len(self.value) == 0:
            return True
        else:
            return False
    def show_Deq(self):
        for x in self.value:
            print(" => ",x  ,end= "  \n")

dq = Deque()
dqq =Deque()
dq.addFront(1)
dq.addFront(2)
dq.addFront(3)
dq.addEnd(6)
dq.addEnd(5)
dq.addEnd(4)
dq.removeFront()
dq.removeFront()
dq.removeEnd()
print(dq.size_Deq())
print(dq.isEmpty())
print(dqq.isEmpty())
dq.show_Deq()

