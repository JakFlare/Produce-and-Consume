from threading import *
from time import *

class Producer:
    def __init__(self):
        self.items = ['apple','melon','orange','grape','pear']
        self.inventory = [0,0,0,0,0]
    def produce(self,item,num):
        self.inventory[item] = num
    def display(self):
        print("-----------------------------------")
        for i in range(len(self.items)):
            print(self.items[i].ljust(8,' '),'  x  ',self.inventory[i])
        print("-----------------------------------")
        print()
    def getItem(self):
        return self.items
    def getInv(self):
        return self.inventory
    def setInv(self,ind,amt):
        self.inventory[ind] = amt
    def subInv(self,ind,amt):
        self.inventory[ind] -= amt



'''
p = Producer()
p.display()
p.produce(0,5)
p.produce(1,2)
p.produce(2,6)
p.produce(3,1)
p.produce(4,8)
p.display()
#p.setInv(0,2)
#p.subInv(2,3)
#p.display()

'''


class Consumer:
    def __init__(self):
        self.order = []
        self.complete = False
        self.order = []
        self.amount = []

    def consume(self,item,num):
        p.display()
        prod = p.getItem()
        inv = p.getInv()
        if inv[item] >= num:
            self.order.append(item)
            self.amount.append(num)
            p.subInv(item,num)
        else:
            print("Not enough inventory. Please select another item.")
        p.display()
        
p = Producer()
for i in range(len(p.items)):
    p.produce(i,10)

c = Consumer()
c.consume(0,12)


