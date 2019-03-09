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
    def swapNode(self,key1,key2):
        if key1==key2:
            print('The two nodes are the same nodes, cannot be swapped')
            return

        prev1=None
        curNode1=self.head
        while curNode1 != None and curNode1.data != key1:
            prev1=curNode1
            curNode1=curNode1.next

        prev2=None
        curNode2=self.head
        while curNode2 != None and curNode2.data != key2:
            prev2=curNode2
            curNode2=curNode2.next

        if curNode1==None or curNode2==None: # scan reaches the end but not found
            print("The nodes doesn't exist in the list")
            return
       
        else: 
            if prev1==None: # key1 is in the head node,key2 is not
                self.head=curNode2
                prev2.next=curNode1
            elif prev2==None:# key2 is not in the head node,key1 is not
                self.head=curNode1
                prev1.next=curNode2
            else: # none are the head node
                prev1.next=curNode2
                prev2.next=curNode1
            
            # swap the .next pointer
            temp1=curNode1.next
            temp2=curNode2.next
            curNode1.next=temp2
            curNode2.next=temp1

    def reverse_iterative(self):
        prev=None
        curNode=self.head
        while curNode!=None:
            nxt_temp=curNode.next
            curNode.next=prev # flip the .next point to point to the front
            # think about why it is not prev=curNode.next?

            prev=curNode
            curNode=nxt
        self.head=prev




lst=linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
#lst.prepend('D')
#lst.deleteNode('A')
#lst.deleteAtPos(0)
#print(lst.len_iterative())
#print(lst.len_recursive(lst.head))
#lst.swapNode('A','C')
#lst.swapNode('A','A')
#lst.swapNode('E','F')
#lst.swapNode('B','C')
#lst.swapNode('A','B')
lst.reverse_iterative()
lst.printList()


        
