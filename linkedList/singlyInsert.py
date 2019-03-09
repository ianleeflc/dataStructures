class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        curNode=self.head
        while curNode!=None:
            print(curNode.data)
            curNode=curNode.next
    def append(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else: 
            lastNode=self.head
            while lastNode.next!=None:
                lastNode=lastNode.next
            lastNode.next=newNode
    def prepend(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else: 
            newNode.next=self.head
            self.head=newNode
    def insertAfterNode(self,prevNode,data):
        newNode=Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode



lst=linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.append('D')
lst.prepend('E')
lst.prepend('f')
lst.insertAfterNode(lst.head.next,'Insrt')
lst.printList()


        
