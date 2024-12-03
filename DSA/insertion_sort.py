def ascending_insertion_sort(arr):
    n = len(arr)  # Get the length of the array

    for i in range(1, n):  # Start from the second element
        key = arr[i]  # The current element to be inserted
        j = i - 1  # Index of the last sorted element

        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move to the next element on the left

        arr[j + 1] = key  # Place key in its correct position

# Example usage
arr = [34, 7, 23, 89, 12]
ascending_insertion_sort(arr)
print(arr)