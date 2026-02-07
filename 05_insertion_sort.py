n=int(input("enter size of array:"))
arr=[]
print(f"enter {n} elements:")
for i in range(n):
    value=int(input())
    arr.append(value)
print("display unsorted array:",arr)

for i in range(1,n):
    insert_index=i
    sorted=arr[i]
    for j in range(i-1,-1,-1):
        if arr[j]>sorted:
            arr[j+1]=arr[j]
            insert_index=j
        else:
            break
    arr[insert_index]=sorted
print("display sorted array:",arr)