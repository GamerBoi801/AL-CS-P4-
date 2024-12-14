def linear_search(arr, target):
    """
    Perform a linear search on the given array.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the target element if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [34, 7, 23, 89, 12, 56, 78, 45, 90, 11]
target = 56
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")