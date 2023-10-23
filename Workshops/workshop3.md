
# Workshop Three: Iterative Algorithms and Efficiencies

Iterative algorithms are a fundamental concept in computer science, where a set of instructions is repeated until a specific condition is met. These algorithms are often used to solve problems that involve processing a collection of data or performing repetitive tasks.

**Efficiency of Iterative Algorithms**

The efficiency of an iterative algorithm is typically measured using Big O notation, which describes how the algorithm's runtime grows as the input size increases. Common Big O notations include:

- **O(1):** Constant time - The runtime does not depend on the input size.

- **O(log n):** Logarithmic time - The runtime grows logarithmically with the input size.

- **O(n):** Linear time - The runtime grows linearly with the input size.

- **O(n log n):** Log-linear time - The runtime grows as a product of linear and logarithmic factors.

- **O(n^2):** Quadratic time - The runtime grows quadratically with the input size.

- **O(2^n):** Exponential time - The runtime grows exponentially with the input size.

**Example 1: Finding the Sum of an Array**

Consider an algorithm that calculates the sum of all elements in an array of 'n' elements.

```python
def sum_array(array):
    total_sum = 0
    for element in array:
        total_sum += element
    return total_sum
```

This algorithm has a linear time complexity of O(n) because it iterates through the array once, performing a constant-time operation (addition) for each element.

**Example 2: Finding the Maximum Value in an Array**

Consider an algorithm that finds the maximum value in an array of 'n' elements.

```python
def find_max(array):
    max_value = array[0]
    for element in array:
        if element > max_value:
            max_value = element
    return max_value
```

This algorithm also has a linear time complexity of O(n) because it iterates through the array once, performing a constant-time operation (comparison) for each element.

**Sorting Algorithms**

Sorting algorithms are used to arrange elements in a specific order, such as ascending or descending order.

**Selection Sort**

Selection sort repeatedly finds the minimum element and places it in its correct position.

```python
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
```

Time complexity: O(n^2)

**Bubble Sort**

Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

```python
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
```

Time complexity: O(n^2)

**Insertion Sort**

Insertion sort builds a sorted sub-array by inserting elements into their correct positions.

```python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
```

Time complexity: O(n^2)

**Searching Algorithms**

Searching algorithms are used to find a specific element within a collection of data.

**Linear Search (Sequential Search)**

Linear search iterates through the elements one by one until the target element is found or the end is reached.

```python
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

Time complexity: O(n)

**Binary Search**

Binary search repeatedly divides the search space in half, comparing the target element to the middle element to determine which half to search next.

```python
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Time complexity: O(log n)

As you can see, the time complexity of sorting and searching algorithms varies depending on the specific algorithm and the input size. Big O notation provides a way to compare the efficiency of these algorithms and choose the most appropriate one for a given task.