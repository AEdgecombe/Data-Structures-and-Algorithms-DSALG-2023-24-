from random import sample

class Recursion:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)
    
    def recurFib(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.recurFib(n - 1) + self.recurFib(n - 2)
        
    def iterFib(self, n):
        f1 = f2 = 1
        out = -1
        if (n == 1 or n == 2):
            return f1
        for i in range(3, n + 1):
            out = f1 + f2
            f1 = f2
            f2 = out
            print("The " + str(i) + "-th Fibbonaci number is " + str(out))
        return out

    def gcd(self, n, m):
        if (n == m):
          return n
        elif (n < m):
          return self.gcd(m - n, n)
        else:
          return self.gcd(n - m, m)

    def mergeSort(self):
      #arr has to be a sorted array
      self._mergeSort(self.data, 0, len(self.data) - 1)
      print("After the merge sort, the array is " + str(self.data))

    def _mergeSort(self, arr, start, end):
      if (start >= end):
        return
      mid = (end - start) // 2 + start
      self._mergeSort(arr, start, mid)
      self._mergeSort(arr, mid + 1, end)
      #Merge the 2 sorted sub-arrays
      self._merge(arr, start, mid, end)

    def _merge(self, arr, start, mid, end):
      temp = []
      p1 = start
      p2 = mid + 1
      #Compare the first elements in two sub-arrays (referenced by p1 and p2 respectively), the smaller one is first inserted to the new array
      while (p1 <= mid and p2 <= end):
        if (arr[p1] < arr[p2]):
          temp.append(arr[p1])
          p1 += 1
        else:
          temp.append(arr[p2])
          p2 += 1
      #When one sub-array is exhausted, the remaining elements of the other sub-array iwll be copied to the new array - only 1 of the following 2 while loops will be executed
      while (p1 <= mid):
        temp.append(arr[p1])
        p1 += 1
      while (p2 <= end):
        temp.append(arr[p2])
        p2 += 1
      #Update the original array
      for i in range(len(temp)):
        arr[start + i] = temp[i]

    def quickSort(self):
      #arr has to be a sorted array
      self._quickSort(self.data, 0, len(self.data) - 1)
      print("After the quick sort, the array is " + str(self.data))

    def _quickSort(self, arr, start, end):
      if (start < end):
      #After the partition, pivot is in its final correct position
        pivot = self._partition(arr, start, end)
        self._quickSort(arr, start, pivot - 1)
        self._quickSort(arr, pivot + 1, end)

    def _partition(self, arr, start, end):
      #We choose the last element as the pivot
      pivot = arr[end]
      i = start
      for j in range(start, end):
        if (arr[j] < pivot):
          #Swap the element smaller than the pivot and the element larger than the pivot - the swapped one with a smaller value has a larger index
          arr[j], arr[i] = arr[i], arr[j]
          i += 1;
      #Now swap the pivot to its final correct position - smaller than right half, larger than left half
      arr[end], arr[i] = arr[i], arr[end]
      return i

    def palindrome(self, s):
      if (len(s) == 0 or len(s) == 1):
        return True
      elif (s[0] != s[len(s) - 1]):
        print("The first is " + s[0])
        print("The last is " + s[len(s) - 1])
        #Not palindrome if the first and last element are different
        return False
      else:
        #Noting the substring returns the interval with an open interval [start, end)
        return self.palindrome(s[1 : len(s) - 1])

    def printAll(self):
      print("The size of the random array " + str(len(self.data)))
      print("Before sorting, the array is " + str(self.data))

    def partition(self, s):
      n = len(s)
      palindromeList = []
      if (n == 0):
        #Stopping case
        palindromeList.append([])
      for i in range(1, n + 1):
        if (s[:i] != s[:i][::-1]):
          continue
        j = [s[:i]]
        s2 = self.partition(s[i:])
        for k in s2:
          #Concatenate the existing palindrome j with the remaining list/array of palindromes k - this will be repeated in recursive calls
          palindromeList.append(j + k)
      return palindromeList

if  __name__ == "__main__":
  arr = Recursion()
  arr.iterFib(10)
  print(arr.recurFib(10))
  print("The greatest common divisor is " + str(arr.gcd(27, 18)))
  arr.initialise()
  arr.printAll()
  arr.mergeSort()
  arr.initialise()
  arr.printAll()
  arr.quickSort()
  str1 = "!_asddsa_!"
  print("The string " + str1 + " is palindrome? --- " + str(arr.palindrome(str1)))
  str2 = "aaa"
  print(arr.partition(str2))