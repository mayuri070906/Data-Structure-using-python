n=int(input("enter size of array:"))
arr=[]
print(f"enter {n} elements:")
for i in range(n):
    value=int(input())
    arr.append(value)
print("display unsorted array:",arr)

for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp

print("display sorted array:",arr)