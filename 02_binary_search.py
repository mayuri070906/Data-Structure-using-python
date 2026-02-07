def binarySearch(arr,targetVal):
    beg=0
    end=len(arr)-1
    while beg<=end:
        mid=(beg+end)//2
        if arr[mid]==targetVal:
            return mid
        if targetVal>arr[mid]:
            beg=mid+1
        else:
            end=mid-1
    return -1
        
n=int(input("enter size of array:"))
arr=[]
print(f"enter {n} elements:")
for _ in range(n):
    value=int(input())
    arr.append(value)
targetVal=int(input("enter value to search:"))
result=binarySearch(arr,targetVal)
if result!=-1:
    print("Found at index",result)
else:
    print("Not found")
