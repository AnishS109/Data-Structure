class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List():
    def __init__(self,head):
        self.head = head

    def addNode_at_starting(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addNode_at_end(self,data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            tail = None
            while curr:
                tail = curr
                curr = curr.next

            tail.next = newNode
            newNode.prev = tail
    
    def addNode_at_position(self,data,posi):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            for i in range(posi-1):
                curr = curr.next    
                if curr is None:
                    raise IndexError("Position is out of Linked List Length")
                
            newNode.next = curr.next
            newNode.prev = curr

            if curr.next:
                curr.next.prev = newNode

            curr.next = newNode


# -------------------------------- DELETING NODE AT STARTTING ------------------------------


def deleteNode_at_start(head):

    if head is None:
        return None
    
    newHead = head.next

    if head.next:
        newHead.prev = None

    head.next = None

    return newHead


# --------------------------------- DELETING NODE AT ENDING ----------------------------------


def deleteNode_at_end(head):

    if head is None:
        return None
    if head.next is None:
        return None
    else:
        curr = head
        while curr.next:
            curr = curr.next

        curr.prev.next = None
        curr.prev = None
        return head
    

# --------------------------------- DELETING NODE AT MIDDLE WITH GIVEN POSITION -------------------------


def deleteNode_at_position(head,position):
    if position == 0:
        newHead = head.next
        if newHead:
            newHead.prev = None
        head.next = None
        return newHead
    
    curr = head

    for i in range(position):
        curr = curr.next
    
    if curr.next is None:
        curr.prev.next = None
        curr.prev = None
    else:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev = None
        curr.next = None

    return head


# --------------------------------- REVERSE DOUBLY LINKED LIST --------------------------------


def reverse(head):
    curr = head
    temp = None

    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        curr = curr.next

    if temp:
        head = temp.prev

    return head


# ------------------------------------ DELETE ALL OCCURRENCE OF THE GIVE ELEMENT "K" ----------------------------------


def deleteAllOccurrences(head, target):
    curr = head
    while curr :
        if curr.val == target:
            if curr.prev is None:
                head = curr.next
                if curr.next:
                    curr.next.prev = None
            elif curr.next is None:
                curr.prev.next = None
                curr.prev = None
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = None
                curr.prev = None
        
        curr = curr.next

    return head


# ----------------------------------- REMOVE DUPLICATES FROM SORTED DOUBLY LINKED LIST ------------------------------------


def removeDuplicated(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            nextt = curr.next

            if nextt.next:
                curr.next = nextt.next
                nextt.next.prev = curr
                nextt.next = None
                nextt.prev = None
            else:
                curr.next.prev = None
                curr.next = None


        else:
            curr = curr.next

    return head


