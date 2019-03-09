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
    def deleteNode(self,key):
        curNode=self.head
        if curNode!=None and curNode.data==key:
            self.head=curNode.next
            curNode=None
            return
        else: 
            prev=None
            while curNode!=None and curNode.data!=key:
                prev=curNode
                curNode=curNode.next
            if curNode==None:
                print('The data is not in the list')
                return
            else: 
                prev.next=curNode.next
                curNode=None

lst=linkedList()
lst.append('A')
lst.prepend('ff')
lst.deleteNode('a')
lst.deleteNode('A')
lst.printList()


        
