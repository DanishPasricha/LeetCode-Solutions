class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        
        if index<0 or index>=self.size: return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size: return 
        
        curr= self.head
        new = ListNode(val)
        if index<=0:
            new.next=self.head
            self.head =  new
        else:
            for i in range(index-1):
                curr = curr.next
            new.next = curr.next  
            curr.next = new
            
        self.size+=1;
            
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size: return 
        
        curr = self.head
        
        if index<=0:
            saved = curr.next
            self.head.next = None
            self.head = saved
        else:
            for i in range(index-1):
                curr = curr.next;
            saved = curr.next.next
            curr.next=None
            curr.next=saved
        self.size-=1
        


        
        
        
        
        
        
        
        
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)