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

