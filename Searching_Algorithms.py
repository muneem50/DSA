                                            # LINEAR SEARCH

def search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
arr = [2, 3, 4, 10, 40]
x = 100
N = len(arr)
result = search(arr, N, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

                                            #  BINARY SEARCH
# Iterative Binary Search                   

def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        else:
            high = mid - 1
    # If we reach here, then the element
    # was not present
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

# Recursive Binary Search Algorithm

# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = low + (high - low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)
    # Element is not present in the array
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")




