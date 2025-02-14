arr = [2, 3, 4, 10, 40]

def binary_search(arr, target):
    """
    performs binary search on a sorted array to find the target value.
    arr: a sorted list of numbers (integers or floats).
    target: value to be searched.

    returns:
        array index of the target value in the array if found, otherwise -1.
    """
    max = len(arr) - 1  # highest possible index
    min = 0  # lowest possible index

    while min <= max:
        mid = (min + max) // 2  # middle index

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            min = mid + 1
        else:
            max = mid - 1

    return False #if target not found


# Corrected usage:  Pass the array *and* the target to the function.
target_value = 40
result = binary_search(arr, target_value)

if result:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array")

"""How does it work?
    The binary search algorithm works by repeatedly dividing the sorted array in half 
    until the target value is found."""