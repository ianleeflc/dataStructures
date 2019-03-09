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
    def deleteAtPos(self,pos):
        curNode=self.head
        if pos==0:
            self.head=curNode.next
            curNode=None
            return
        else: 
            cnt=0
            prev=None
            while curNode != None and cnt != pos:
                prev=curNode
                curNode=curNode.next
                cnt+=1
            if curNode==None:
                print("The node doesn't exist") # maybe the index is longer than the list
                return
            else: 
                prev.next=curNode.next
                curNode=None
    def len_iterative(self):
        cnt=0
        curNode=self.head
        while curNode != None:
            curNode=curNode.next
            cnt+=1
        return cnt
    def len_recursive(self,headNode):
        if headNode is None: 
            return 0
        else: 
            return 1+self.len_recursive(headNode.next)




lst=linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.prepend('ff')
#lst.deleteNode('A')
#lst.deleteAtPos(0)
print(lst.len_iterative())
print(lst.len_recursive(lst.head))
lst.printList()


        
