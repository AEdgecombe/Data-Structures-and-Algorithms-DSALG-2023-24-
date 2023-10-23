# Recursive Algorithms

## Mergesort

Pseudocode for Merge Sort:

```
function mergeSort(array)
    if length(array) <= 1
        return array
    else
        leftHalf = array[0 to length(array)/2]
        rightHalf = array[length(array)/2 + 1 to length(array)-1]
        
        sortedLeft = mergeSort(leftHalf)
        sortedRight = mergeSort(rightHalf)
        
        return merge(sortedLeft, sortedRight)
    end if
end function

function merge(leftArray, rightArray)
    result = []
    while length(leftArray) > 0 and length(rightArray) > 0
        if leftArray[0] <= rightArray[0]
            append leftArray[0] to result
            leftArray = leftArray[1 to length(leftArray)-1]
        else
            append rightArray[0] to result
            rightArray = rightArray[1 to length(rightArray)-1]
        end if
    end while
    
    if length(leftArray) > 0
        append leftArray to result
    else
        append rightArray to result
    end if
    
    return result
end function
```

Explanation of each part:

1. `mergeSort(array)`: This is the main function that calls itself recursively to sort the array. It first checks if the array has only one element, in which case it is already sorted and returns the array. Otherwise, it splits the array into two halves and calls `mergeSort` on each half.

2. `leftHalf = array[0 to length(array)/2]`: This line creates a new array called `leftHalf` that contains the first half of the original array.

3. `rightHalf = array[length(array)/2 + 1 to length(array)-1]`: This line creates a new array called `rightHalf` that contains the second half of the original array.

4. `sortedLeft = mergeSort(leftHalf)`: This line calls `mergeSort` on the `leftHalf` array to sort it.

5. `sortedRight = mergeSort(rightHalf)`: This line calls `mergeSort` on the `rightHalf` array to sort it.

6. `return merge(sortedLeft, sortedRight)`: This line calls the `merge` function to merge the sorted `leftHalf` and `rightHalf` arrays into a single sorted array.

7. `merge(leftArray, rightArray)`: This function merges two sorted arrays into a single sorted array. It first creates an empty array called `result`. Then, it compares the first elements of `leftArray` and `rightArray` and appends the smaller element to `result`. It repeats this process until one of the arrays is empty. Finally, it appends the remaining elements of the non-empty array to `result` and returns `result`.

## Quicksort

Pseudocode for Quicksort:

```
function quickSort(array, low, high)
    if low < high
        pivotIndex = partition(array, low, high)
        quickSort(array, low, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, high)
    end if
end function

function partition(array, low, high)
    pivot = array[high]
    i = low - 1
    
    for j = low to high - 1
        if array[j] <= pivot
            i = i + 1
            swap array[i] with array[j]
        end if
    end for
    
    swap array[i + 1] with array[high]
    return i + 1
end function
```

Explanation of each part:

1. `quickSort(array, low, high)`: This is the main function that calls itself recursively to sort the array. It first checks if the `low` index is less than the `high` index, which indicates that there are elements to sort. If so, it partitions the array around a pivot element and then recursively sorts the subarrays to the left and right of the pivot.

2. `pivotIndex = partition(array, low, high)`: This line calls the `partition` function to partition the array around a pivot element and returns the index of the pivot.

3. `quickSort(array, low, pivotIndex - 1)`: This line recursively calls `quickSort` to sort the subarray to the left of the pivot.

4. `quickSort(array, pivotIndex + 1, high)`: This line recursively calls `quickSort` to sort the subarray to the right of the pivot.

5. `partition(array, low, high)`: This function partitions the array around a pivot element and returns the index of the pivot. It chooses the last element as the pivot and maintains two pointers: `i` and `j`. It iterates through the array, swapping elements that are less than or equal to the pivot with elements to the left of `i`. Finally, it swaps the pivot with the element at `i + 1` and returns `i + 1` as the pivot index.

6. `pivot = array[high]`: This line selects the last element of the array as the pivot.

7. `i = low - 1`: This line initializes the `i` pointer to one position before the `low` index.

8. `for j = low to high - 1`: This loop iterates through the array from the `low` index to the `high - 1` index.

9. `if array[j] <= pivot`: This conditional statement checks if the current element is less than or equal to the pivot.

10. `i = i + 1`: This line increments the `i` pointer.

11. `swap array[i] with array[j]`: This line swaps the current element with the element at the `i` position, effectively moving smaller elements to the left of `i`.

12. `swap array[i + 1] with array[high]`: This line swaps the pivot with the element at `i + 1`, placing the pivot in its correct position.

13. `return i + 1`: This line returns the index of the pivot.

## Binary Search

Pseudocode for Binary Search:

```
function binarySearch(array, target, low, high)
    if low > high
        return -1
    else
        mid = (low + high) / 2
        if array[mid] == target
            return mid
        else if array[mid] < target
            return binarySearch(array, target, mid + 1, high)
        else
            return binarySearch(array, target, low, mid - 1)
        end if
    end if
end function
```

Explanation of each part:

1. `binarySearch(array, target, low, high)`: This is the main function that recursively searches for the target element in the sorted array. It takes the array, target element, and the low and high indices of the search range as parameters.

2. `if low > high`: This conditional statement checks if the search range is empty, indicating that the target element is not found. If so, it returns -1.

3. `mid = (low + high) / 2`: This line calculates the middle index of the search range.

4. `if array[mid] == target`: This conditional statement checks if the element at the middle index is equal to the target element. If so, it returns the middle index as the position of the target element.

5. `else if array[mid] < target`: This conditional statement checks if the element at the middle index is less than the target element. If so, it recursively calls `binarySearch` to search for the target element in the upper half of the search range.

6. `else`: This else block handles the case where the element at the middle index is greater than the target element. It recursively calls `binarySearch` to search for the target element in the lower half of the search range.

7. `return binarySearch(array, target, mid + 1, high)`: This line recursively calls `binarySearch` to search for the target element in the upper half of the search range, starting from the index after the middle index.

8. `return binarySearch(array, target, low, mid - 1)`: This line recursively calls `binarySearch` to search for the target element in the lower half of the search range, ending at the index before the middle index.