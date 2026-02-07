def linearSearch(arr,key):
    n=len(arr)
    i=0
    while i<n:
        if arr[i]==key:
            return i
        else:
            i+=1
    return -1

n=int(input("enter size of array:"))
arr=[]
print(f"enter {n} elements:")
for _ in range(n):
    value=int(input())
    arr.append(value)

key=int(input("enter value to search:"))
result=linearSearch(arr,key)
if result!=-1:
    print("Found at index",result)
else:
    print("NOT Found")