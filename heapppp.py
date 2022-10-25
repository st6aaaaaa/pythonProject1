
class Node:

    def __init__(self,key):
        self.iData = key

    def getKey(self):
        return self.iData

    def setKey(self,id):
        self.iData = id

class Heap:

    def __init__(self, mx):
        self.maxSize = mx
        self.currentSize = 0
        self.heapArray = [None] * self.maxSize


    def isEmpty(self):
        return (self.currentSize == 0)

    def insert(self,key):

        if self.currentSize  == self.maxSize:
            return False

        newNode = Node(key)
        self.heapArray[self.currentSize] = newNode

        self.Up(self.currentSize)
        self.currentSize += 1
        return True

    def Up(self,index):
        parent = (index -1)//2
        bottom = self.heapArray[index]
        while index>0 and self.heapArray[parent].getKey() < bottom.getKey():
            self.heapArray[index] = self.heapArray[parent]
            index = parent
            parent = (parent -1) //2
        self.heapArray[index] = bottom


    def remove(self):

        root = self.heapArray[0]
        self.currentSize -=1
        self.heapArray[0] = self.heapArray[self.currentSize]
        self.vniz(0)
        return root

    def vniz(self,index):

        largerChild = None
        top = self.heapArray[index]
        while index < (self.currentSize//2):
            leftChild = 2*index + 1
            rightChild = leftChild +1

            if rightChild <self.currentSize and self.heapArray[leftChild].getKey() <self.heapArray[rightChild].getKey() :
                largerChild = rightChild
            else:
                largerChild = leftChild

            if top.getKey() >= self.heapArray[largerChild].getKey():
                break
            self.heapArray[index] = self.heapArray[largerChild]
            index = largerChild
        self.heapArray[index] = top

    def change(self,index,newValue):
        if index<0 or index>=self.currentSize:
            return False
        oldValue = self.heapArray[index].getKey()
        self.heapArray[index].setKey(newValue)

        if oldValue <newValue:
            self.Up(index)
        else:
            self.vniz(index)
        return True

    def display(self):
        for i in range(self.currentSize):
            if self.heapArray[i] is not None:
                print(self.heapArray[i].getKey(), end = " " )



theHeap = Heap(31)
theHeap.insert(30)
theHeap.insert(20)
theHeap.insert(100)
theHeap.insert(90)
theHeap.insert(34)
theHeap.insert(89)
theHeap.insert(56)
theHeap.insert(35)
theHeap.insert(3)
theHeap.display()


print()

theHeap.remove()
theHeap.display()

print()

theHeap.change(3 ,140)
theHeap.display()