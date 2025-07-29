'''#ARRay operations
#program to conside list arr=[10,20,30,40]and perform insert operation and
deletion operation with 50 and 25at position 2 respectively delete 30 and traverse the array to fetech the number 25 is present
or not'''

arr=[10,20,30,40]
#insert
arr.append(50)
arr.insert(2,25)
print(arr)
#deletion
arr.remove(30)
arr.pop()
print(arr)
#traversal
for i in arr:
    print(i, end=' ')
#searching
print("\n 25 in array?", 25 in arr)



'''program to check wheather the given string is palindrome or not
count the palindromic charcters repeated count 
str=madam
output: {'m':2, 'a':2, 'd':1}
'''
text= input("enter a name:")
if text==text[::-1]:
    print("TRUE")
else:
    print("FALSE")
freq={}
for ch in text:
    freq[ch]= freq.get(ch,0)+1
print(freq)    



SEARCHINGS
linear
binary
sentinel search
Fibonacci search
interpolation search


LINEAR SEARCH:  in sorted or unsorted arrays
[45,-9,77,32]
1.arr of list of size n
2.key for search element
3.start with zero index 
4.compare arr[i]==key
         arr[i] = key return index
         else not(move to next index)

5.repeat same steps till n-1
6.if no match return -1
#program
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
size= int(input("enter size of the array:"))
arr=[]
print("enter the elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    arr.append(num)
key = int(input("enter the element to search:"))
result= linear_search(arr,key)
if result!= -1:
    print(f"\n element {key} found at {result}")
else:
    print(f"\n element {key} not found in array")


BINARY SEARCH:
1.array must be sorted
2.array is divided into two separate equilant halfs
set low & high 0->n-1
condition low<=high
mid= low+high//2
arr[mid]==key return mid
arr[mid<key low mid+1
arr[mid]>key high mid-1
not found return -1
#program
def binary_search(arr,key):
    low=0
    high= len(arr)-1
    while low<=high:
        mid= (low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low= mid+1
        else:
            high= mid-1
            
    return -1
size= int(input("enter size of the array:"))
arr=[]
print("enter the elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    arr.append(num)
key = int(input("enter the element to search:"))
result= binary_search(arr,key)
if result!= -1:
    print(f"\n element {key} found at {result}")
else:
    print(f"\n element {key} not found in array")


JUMP SEARCH:
#jump search
import math
def jump_search(arr,target):
    if not arr:
        return -1
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[prev]<target:
        prev +=step
    for i in range(max(0,prev-step),min(n,prev+1)):
        if arr[i] == target:
            return i
    return -1
arr = [1,3,4,7,9,11,22,25]
target = 4
result = jump_search(arr,target)
print(result)


EXPONENTIAL SEARCH:
#exponential search
def bsearch_range(arr,target,left,right):
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <target:
            left = mid+1
        else:
            right = mid-1
    return -1
def expo_search(arr,target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i<n and arr[i]<=target:
        i *=2
    return bsearch_range(arr,target,i//2,min(i,n-1))
arr = [2,4,6,8,10,12,14,16]
target = 14
result = expo_search(arr,target)
print(f"Element {target} found at index:{result}")




FIBONACI SEARCH:
#fibonaci search
def fibsearch(arr, target):
    if not arr:
        return -1

    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    # Find the smallest Fibonacci number >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    # Final check for last element
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

# Test
arr = [2, 4, 6, 8, 10, 12, 13]
target = 10
result = fibsearch(arr, target)
print(f"Element {target} found at index: {result}")



BUBBLE SORT:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
size = int(input())
arr = []
print("Enter the elements: ")
for _ in range(size):
    arr.append(int(input()))
print("Original list: ",arr)
bubble_sort(arr)
print("BubbleSorted: ",arr)


COUNTING SORT:

def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0]*(max_val+1)
    #freq
    for num in arr:
        count[num]+=1
    #count
    for i in range(1,len(count)):
        count[i]+= count[i-1]
    output = [0] * len(arr)
    #stable sort
    for num in reversed(arr):
        output[count[num]-1] = num
        count[num] -=1
    #coping sorted list
    for i in range(len(arr)):
        arr[i] = output[i]
arr = [4,2,2,8,9,3,2,1,6,5,3]
print("Before Sorting: ",arr)
counting_sort(arr)
print("After Sorting: ",arr)



def count_sort(arr,exp):
    n = len(arr)
    output = [0]*n
    count = [0] * 10 #for digits 0 to 9
    for i in range(n): #frequencies of units position of numbers
        index = (arr[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]//exp)%10
        output[count[index]-1] = arr[i]
        count[index] -=1
        i -=1
    
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp>0:
        count_sort(arr,exp)
        exp *=10
arr = [170,45,75,90,802,24,2,66]
print("Before sort ",arr)
radix_sort(arr)
print("After sort",arr)


#PANCAKE SORT:

def flip(arr,k):
    return arr[:k+1][::-1]+ arr[k+1:]
def pancake(arr):
    n = len(arr)
    for size in range(n,1,-1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size-1:
            if max_index !=0:
                arr = flip(arr,max_index)
                print(f"Flip at {max_index+1}: {arr}")
            arr = flip(arr,size-1)
            print(f"Flip at {size}: {arr}")
    return arr
nums = list(map(int,input("enter").split()))
sorted_nums = pancake(nums)
print("Sorted",sorted_nums)






#1.Exception - for base classes
#2.ArithmeticError - math errors
#3.ZeroDivisionError - arises when divided by Zero
#4.StopIteration - next method or iterator not availaile / condition not available
#5.SystemExit - current os exit
#6.StandardError = pre defined keywords
#7.EOFError = i/o till the endoffile
#8.ImportError = file existing errors
#9.KeyboardInterrupt = execution interrupt
#10.NameError-
#11.ValueError = 
#12.IndexError = 
#13.TypeError = 
#14.IOError = 
#15.SyntaxError = 
#16.RuntimeError = 
#17.IndentationError = 
#18.AttributeError = 
#19.AssertionError =  


try:
    ----statements
    ------------
    ------------
except --------:


PROGRAM:

try:
    num1=int(input("enter numerator:"))
    num2=int(input("enter numerator:"))
    output=num1/num2
    print("result:",output)
except ZeroDivisionError:
    print("cannot divide by zero....")



try:
    filename=input("enter the file name:")
    file=open(filename, 'r')
    number=int(file.readline())
    print("number from file",number)
    file.close()
except  FileNotFoundError:
    print("file does not exist....")
except ValueError:
    print("file does not have integer...")
except:
    print("unknow error....")



try:
    num=int(input("enter a number:"))
    print(num**3)
except (KeyboardInterrupt,ValueError,TypeError):
    print("please check before executing....")
print("program terminated....") 




import math
try:
    num=int(input("enter a number:"))
    if num<0:
        raise ValueError("negative number....")
except ValueError:
    print("enter postive number only....")
else:
    print("SquareRoot:",round(math.sqrt(num),4))






LINKED List: non contagious ds


memory allocate
access
1.single ll
2.double ll
3.circular s/d ll

SINGLE LINKED LIST:

head--->node1--->node2--->tail/null

class node:
          def __init___(self,data):
                  self.data=data
                  self.next=none
                  
Insertion operations:

1.at begin
2.at end
3.at location


#PROGRAM: AT BEGIN

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iab(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        print(f"{data} inserted from begin.")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iab(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3")




#AT END:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(f"{data} imserted at end /will be first node")
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        print(f"{data} inserted at end / will be the last node")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3")



#AT POSITION:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iap(self,data,pos):
        newnode=Node(data)
        if pos<=0:
            print("position min>=1")
            return
        if pos==1: #begin start
            newnode.next=self.head
            self.head=newnode
            print(f"{data} inserted at pos-1")
            return
        current=self.head  
        c=1
        while current and c < pos-1:
            current=current.next
            c+=1
        if not current:
            print("not in range...")
            return
        newnode.next=current.next
        current.next=newnode
        print(f"{data} inserted at position{pos}. ")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        pos=int(input("enter position starting from 1"))
        ll.iap(data,pos)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3")



#ELEMENT PRESENT OR NOT IN LL:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
    def search(self,key):
        pos=1
        current=self.head
        while current:
            if current.data==key:
                print(f"{key} found in a LL")
                return True
            current=current.next
            pos+=1
            print(f"{key} not  found in a LL")
            
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3.search")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        val=int(input("enter the value ,you want to search:"))
        ll.search(val)
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")


DELETING OPERATIONS :
1.at end
2.at beginning
3.by value

head--->10--->20--->30--->40--->NULL




#DELETE OPERATION BY VALUE:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode    
    def deletevalue(self,key):
        current=self.head
        if not current:
            print("empty ll")
            return
        if current.data==key:
            self.head=current.next
            print(f"{key} delete from the list")
            return
        prev=None
        while current and current.data!=key:
            prev=current
            current=current.next
        if not current:
            print(f"{key} not found in ll")
            return
        prev.next=current.next
        print(f"{key} deleted from the ll")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. delete by value")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        key=int(input("enter the value ,you want to delete:"))
        ll.deletevalue(key)
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")


#DELETE OPERATION AT BEGIN:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode    
    def deletebegin(self,key):
        if self.head is None:
            print("empty=ll")
        else:
            print("deleted node from begining:",self.head.data)
            self.head=self.head.next
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. at begin")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        ll.deletebegin(key)
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")



#DELETE OPERATION AT END:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode    
    def deleteend(self):  
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            print("Deleted node from end:", current.next.data)
            current.next = None
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. at end")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        ll.deleteend()
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")



#ATM:

class Transaction:
    def __init__(self,transaction_type,amount):
        self.type=transaction_type
        self.amount=amount
        self.next=None
class TransactionHistory:
    def __init__(self):
        self.head=None
    def add_transaction(self,transaction_type,amount):
        nn=Transaction(transaction_type,amount)
        if not self.head:
            self.head=nn
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
        print(f"{transaction_type} of Rs.{amount} recorded....")
    def show_history(self):
        if not self.head:
            print("No Transaction found")
            return 
        print("\n Transaction History ")
        current=self.head
        count=1
        while current:
            print(f"{count},{current.type}-RS{current.amount}")
            current=current.next
            count+=1
history=TransactionHistory()
while True:
    print("\n--------ATM Transaction menu-------")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.History")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=='1':
        amount=float(input("enter amount to deposit:"))
        history.add_transaction("Deposit",amount)
    elif choice=='2':
        amount=float(input("enter amount to withdraw:"))
        history.add_transaction("WithDraw",amount)
    elif choice=='3':
        history.show_history()
    elif choice=='4':
        print("End of transaction.....Exit!!!")
        break
    else:
        print("choose 1/2/3/4 only.....")




CONSIDER A SINGLE LINKED LIST WITH INSERT AT THE END NODES AND
AFTER INSERTION REVERSE THE NODE TO PRINT
INPUT-11-22-33-44-55-NULL
OUTPUT-55-44-33-22-11-NULL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="-")
            temp = temp.next
        print("null")
ll = LinkedList()
for value in [11, 22, 33, 44, 55]:
    ll.insert_end(value)

ll.reverse()
ll.print_list()




DOUBLE LINKED LIST:

opeations
1.insertion  -at begin,end,position
2.deletion   -by value
3.traversal  -forward/backward 

head--->node1--->node2--->node3--->null

node:
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


1.INSERTION :
#at the end insertion at DLL:

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def display(self):
        temp=self.head
        print("double linked list")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DoubleLinkedList()
n=int(input("enter a number of elements:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iae(val)
dll.display()    




# at the begin insertion at DLL:

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def iab(self, data): 
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iab(val)  
dll.display()






#at the position insertion at DLL:

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def iap(self,pos, data): 
        newnode = Node(data)
        if pos<=0:
            print("invalid position")
            return
        if pos==1:
            newnode.next=self.head
            if self.head:
                self.head.prev=newnode
            self.head=newnode
            return
        temp=self.head
        for _ in range(pos-2):
            if temp is None:
                print("position off range")
                return
            temp=temp.next
        if temp is None:
            print("no elements....")
            return
        newnode.next=temp.next
        newnode.prev=temp
        if temp.next:
            temp.next.prev=newnode
        temp.next=newnode    

    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
dll.iap(1,100)
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    pos=int(input(f"enter the position to insert {val}:"))
    dll.iap(pos,val)  
dll.display()



2.DELETION:

1.delete at begin/insert at begin
2.delete at begin/insert at end



#deleteion at begin in double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def dab(self):
        if not self.head:
            print("can't perform delete in an empty list...")
        print(f"deleted: {self.head.data}")
        self.head=self.head.next
        if self.head:
            self.head.prev=None
    def display(self):
        temp=self.head
        print("double linked list")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DoubleLinkedList()
n=int(input("enter a number of elements to insert at end:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iae(val)
dll.display() 
d=int(input("/n hoe many times you want to perform delete op:"))
for _ in range(d):
    dll.dab()
    dll.display()




#delete by value in double linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data): 
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
    def dbv(self, value):
        if not self.head:
            print("Cannot perform delete in an empty list...")
            return
        temp = self.head
        if temp.data == value:
            print(f"Deleted: {temp.data}")
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        while temp and temp.data != value:
            temp = temp.next
        if not temp:
            print(f"Value {value} not found in the list.")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        print(f"Deleted: {temp.data}")
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")
dll = DoubleLinkedList()
n = int(input("Enter number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iae(val)
dll.display()
d = int(input("\nHow many times you want to perform delete operation (by value)? "))
for _ in range(d):
    value = int(input("Enter value to delete: "))
    dll.dbv(value)
    dll.display()













