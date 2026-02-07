def merge(arr,beg,mid,end):
    temp=[0]*len(arr)
    i=beg
    j=mid+1
    k=beg
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            j+=1
        k+=1
    while i<=mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j<=end:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(beg,end+1):
        arr[i]=temp[i]


def divide(arr,beg,end):
    if beg<end:
        mid=(beg+end)//2
        divide(arr,beg,mid)
        divide(arr,mid+1,end)
        merge(arr,beg,mid,end)
size=int(input("enter size of array:"))
arr=[]
print(f"enter {size} element:")
for i in range(size):
    value=int(input())
    arr.append(value)
print("display before sorted array:",arr)
divide(arr,0,size-1)
print("display after sorted array:",arr)
