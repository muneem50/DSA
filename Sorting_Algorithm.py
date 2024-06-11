                            # BUBBLE SORT 01-06-2024
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('Binary Sorted Array',arr)
                
unsorted_list=[9,1,6,3,19,0]
print('Unsorted Array ', unsorted_list, '\n')
bubble_sort(unsorted_list)

#                             # SELECTION SORT

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [9,1,6,3,19,0]
selection_sort(arr)
print("Selection Sorted array is:", arr)

                              # Insertion Sort 

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    print('Insertion Sorted Array:',arr)

arr = [9,1,6,3,19,0]
insertionSort(arr)

                               # Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    # Merge left and right halves into result array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    # Append any remaining elements from left and right halves
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

arr = [9,1,6,3,19,0]
sorted_arr = merge_sort(arr)
print("Merge Sorted array:", sorted_arr)

                                  # QUICK SORT

def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
             # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
# Find pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

array = [9,1,6,3,19,0]
N = len(array)
quicksort(array, 0, N - 1)
print('Quick Sorted array:',array)
