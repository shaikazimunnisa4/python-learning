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
print(f"Element {target} found at index: {result}")"""



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
print("After Sorting: ",arr)"""



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
print("Sorted",sorted_nums)"""

