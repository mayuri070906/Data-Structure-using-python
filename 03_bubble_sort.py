n=int(input("enter size of array:"))
arr=[]
print(f"enter {n} element:")
for i in range(n):
    value=int(input())
    arr.append(value)
print("display unsorted array:",arr)

for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] =temp
            swapped=True
    if not swapped:
        break
print("display sorted array:",arr)
