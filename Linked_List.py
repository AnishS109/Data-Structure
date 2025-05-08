# ---------------------- CREATING A NODE ---------------------------

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# ---------------------- CREATING A LINKED LIST --------------------

class Linked_List:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

# ------------------------ PRINTING ALL NODES OF LINKED LIST -------------------------


l1 = Linked_List()

l1.add_node(value=10)
l1.add_node(value=20)
l1.add_node(value=30)

# print(l1.head.data)
# print(l1.head.next.data)

def print_LL(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

# print_LL(l1.head)


# ------------------------ FIND LENGTH OF A LINKED LIST ------------------------------


l2 = Linked_List()

l2.add_node(value=1)
l2.add_node(value=2)
l2.add_node(value=3)
l2.add_node(value=4)

def countNode(head):
    c = 0
    if head is None:
        return c
    else:
        current = head
        while current is not None:
            c+=1
            current = current.next

    return c


# ------------------------- ADD ELEMENT AT STARTING ---------------------------

class Nodes:
    def __init__(self,values):
        self.data = values
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def addNode(self, values):
        newNode = Nodes(values)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = newNode

l3 = LL()

l3.addNode(values=2)
l3.addNode(values=3)
l3.addNode(values=4)

def addNode_at_start(head,X):
    Xnode = Nodes(X)
    Xnode.next = head
    return Xnode.data

# print(addNode_at_start(l3.head,1))

# --------------------------- ADD ELEMENT AT ENDING ------------------------


l4 = LL()

l4.addNode(values=1)
l4.addNode(values=2)
l4.addNode(values=3)

def addNode_at_end(head,X):
    Xnode = Node(X)
    current = head
    while current.next is not None:
        current = current.next
    current.next = Xnode
    return head


# ----------------------------- ADD ELEMENT AT PARTICULAR PLACE --------------------------------


l5 = LL()

l5.addNode(values=1)
l5.addNode(values=2)
l5.addNode(values=4)

def addNode_at_middle(head,middle,X):
    Xnode = Node(X)
    current = head

    while current is not None:
        if current == middle:
            Xnode.next = current.next

        current = current.next

    return head


# ------------------------------ DELETING AN ELEMENT IN LINKED LIST --------------------------


l6 = LL()

l6.addNode(values=1)
l6.addNode(values=2)
l6.addNode(values=3)
l6.addNode(values=4)
l6.addNode(values=5)

def deleteNode(head,X):

    if head is not None and head.data == X:
        return head.next
    
    current = head
    prev = None

    while current is not None:
        if current.data == X:
            prev.next = current.next
            break
        prev = current
        current = current.next

    return head


# ---------------------- PRINTING MIDDLE OF THE LINKED LIST -------------------------------


def middleNode(head):
    temp = head
    c = 0
    while temp is not None:
        c += 1
        temp = temp.next

    middle = (c//2) + 1
    temp = head

    while temp is not None:
        middle = middle - 1
        if middle == 0:
            break
        temp = temp.next

    return temp


# ------------------------ REVERSE A LINKED LIST ---------------------------


def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    return prev


# ----------------------------- DETECT CYCLE IN A LINKED LIST --------------------------


def detectCycle(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False


def optimizedDetectCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False


# ------------------------------ DETECT NODE WHERE THE CYCLE STARTS ---------------------------

l0 = LL()

l0.addNode(values=3)
l0.addNode(values=2)
l0.addNode(values=0)
l0.addNode(values=4)
l0.addNode(values=2)

def detectNode(head):
    visited = set()
    current = head

    while current:

        if current in visited:
            return current
        visited.add(current)
        current = current.next


def optimizeDetectNode(head):

    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

                if fast == slow:
                    return slow
        
    return None


# ------------------------ CHECK GIVE LINKED LIST IS PALINDROME OR NOT -------------------------


def isPalindrome(head):
    arr = []
    curr = head

    while curr:
        arr.append(curr.data)
        curr = curr.next

    n = len(arr)

    for i in range(n//2 + 1):
        if arr[i] == arr[(n-1)-i]:
            continue
        else:
            return False

    return True


# --------------------------- ODD EVEN LINKED LIST ----------------------------


def oddEven(head):
    odd = head
    even = head.next
    evenhead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenhead
    return head


# ---------------------------- DELETE Nth NODE IN LINKED LIST -----------------------------


def deleteNode(head,n):
    current = head 
    c = 1

    while current:
        c += 1
        current = current.next

    current = head
    prev = None
    while c>=n:
        c -= 1

        if c == n:
            if prev is None:
                return head.next
            else:
                prev.next = current.next
                return head
            
        else:
            prev = current
            current = current.next


# ------------------------------- DELETE MIDDLE NODE OF THE LINKED LIST ---------------------------


def deleteMiddle(head):
    current = head
    c = 1

    while current:
        c += 1
        current = current.next

    prev = None
    current = head
    middle = c//2

    while c>=middle:
        c -= 1

        if c == middle:
            prev.next = current.next
            return head
        else:
            prev = current
            current = current.next


# ------------------------------- FIND INTERSECTION POINT BETWEEN TWO LL ------------------------------


def intersection(headA,headB):
    currentA = headA
    currentB = headB

    while currentA != currentB:
        if currentA is not None:
            currentA = currentA.next
        else:
            currentA = headB

        if currentB is not None:
            currentB = currentB.next
        else:
            currentB = headA

    return currentA


# --------------------------------- SORT THE LINKED LIST ----------------------------------


def sortLinkedList_Bubble_Sort(head):
    i = head

    while i:
        j = i.next

        while j:
            if i.data > j.data:
                i.data,j.data = j.data,i.data
            else:
                j = j.next

        i = i.next

    return 


# --------------------------------- ADD ONE TO LINKED LIST VALUE --------------------------


def addOne(head):
    curr = head
    num_str = ""

    while curr:
        num_str += str(curr.data)
        curr = curr.next

    num = int(num_str) + 2
    new_str = str(num)

    new_head = Node(int(new_str[0]))
    curr = new_head

    for i in range(1,len(new_str)):
        curr.next = Node(int(new_str[i]))
        curr = curr.next

    return new_head


# ---------------------------------- ROTATE A LINKED LIST -------------------------


def rotate(head,k):
    if not head or not head.next or k==0:
        return head
    
    arr = []
    curr = head

    while curr:
        arr.append(curr.data)
        curr = curr.next    

    n = len(arr)
    temp = [None] * n

    for i in range(n):
        temp[(i+k)%n] = arr[i]

    newhead = Node(temp[0])
    curr = newhead

    for i in range(1,n):
        curr.next = Node(temp[i])
        curr = curr.next

    return newhead


def optmizedRotate(head,k):
    tail = None
    n = 0
    curr = head

    while curr:
        n += 1
        tail = curr
        curr = curr.next

    k = k%n

    if k%n == 0:
        return head
    else:
        tail.next = head
        newLastNodeSteps = n-k
        newTail = head

        while newLastNodeSteps != 0:
            newLastNodeSteps -= 1

            if newLastNodeSteps == 0:
                head = newTail.next
                newTail.next = None
                break
            newTail = newTail.next

    return head


# ------------------------------------ REVERSED LINKED LIST NODES AFTER K INTERVALS --------------------------


def reverseNode(head,k):
    arr = []
    curr = head

    while curr:
        arr.append(curr.data)
        curr = curr.next

    n = len(arr)

    for i in range(0,n,k):
        if i + k <= n:
            arr[i:i+k] = reversed(arr[i:i+k])

    newHead = Node(arr[0])
    curr = newHead

    for i in range(n):
        curr.next = Node(arr[i])
        curr = curr.next

    return newHead


