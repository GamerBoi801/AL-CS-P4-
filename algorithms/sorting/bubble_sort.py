arr = [34, 7, 23, 89, 12, 56, 78, 45, 90, 11, 67, 3, 22, 49, 5, 88, 14, 36, 74, 27]

n = len(arr)
def ascending_bubble_sort(arr):
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                # Swap the elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

#only the conditional sign is reversed for descending order
def descending_bubble_sort(arr):
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] < arr[j + 1]:
                # Swap the elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(descending_bubble_sort(arr))
print(ascending_bubble_sort(arr))