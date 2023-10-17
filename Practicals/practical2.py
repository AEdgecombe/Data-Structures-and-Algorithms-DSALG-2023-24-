def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key

def bubble_sort(array):
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(array) - 1):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = True
