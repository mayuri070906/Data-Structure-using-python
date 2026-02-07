# Partition function
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while True:
        # Move i forward
        while i <= high and arr[i] <= pivot:
            i += 1

        # Move j backward
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, break
        if i >= j:
            break

        # Swap a[i] and a[j]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


    # Swap pivot with arr[j]
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp


    return j


# QuickSort function
def quicksort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quicksort(arr, low, j - 1)
        quicksort(arr, j + 1, high)


# Main logic
size = int(input("Enter size of array: "))
arr = []

print(f"Enter {size} elements:")
for _ in range(size):
    arr.append(int(input()))

print("\nArray before sorting:", arr)

quicksort(arr, 0, size - 1)

print("Array after sorting:", arr)
