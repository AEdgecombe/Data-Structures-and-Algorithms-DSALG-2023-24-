# Introduction to Data Structures Applications: Stacks and Queues

Three keywords throughout the module: Efficiency, Trade-off and Tools

## 1.1 What is a Data Structure 

**What is a Data Structure?**

*A data structure is a specific way of organizing and storing data in a computer to facilitate efficient access and manipulation. It provides a framework for managing data elements and their relationships, enabling efficient operations like searching, insertion, deletion, and sorting. Data structures play a vital role in various applications, including databases, operating systems, and algorithms, as they provide the foundation for efficient data management and manipulation.*

**What is an Algorithm?**

*An algorithm is a precise and finite set of instructions or steps for solving a specific problem or performing a particular task. It's like a detailed recipe for a computer or a person to follow, ensuring a consistent and effective outcome. Algorithms are fundamental in computer science, providing the logical structure for problem-solving, task automation, and computational processes.*


### Activity 1.1

**Explain why an array is an example of a simple data structure?**

An array is considered a fundamental data structure in computer science due to its ability to organize and store data in a specific and efficient manner. It exemplifies the core characteristics of a data structure:

Organization: Arrays provide a structured way to arrange data elements in a contiguous block of memory. Each element is assigned a unique index, allowing direct access to any element without traversing the entire array.

Data Management: Arrays can store a collection of elements of the same data type, such as integers, characters, or strings. This uniformity simplifies data management and enables efficient operations.

Efficient Access: Arrays excel in providing random access to elements, meaning any element can be accessed directly using its index in constant time, regardless of its position in the array.

Basic Operations: Arrays support fundamental operations like insertion, deletion, and searching. While insertion and deletion may require shifting elements, searching can be performed efficiently using various algorithms.

Memory Efficiency: Arrays utilize memory efficiently by storing elements in contiguous memory locations. This arrangement allows for faster access and reduces memory overhead.

Versatility: Arrays are versatile and can be used for various purposes, such as storing numerical data, representing text strings, or implementing matrices for mathematical computations.

Foundational Role: Arrays serve as a building block for more complex data structures, such as linked lists, stacks, and queues. Understanding arrays is essential for grasping more advanced data organization concepts.

In summary, arrays are considered a prime example of a data structure due to their ability to organize, store, and manage data efficiently, providing a foundation for various computational tasks and algorithms.

## 1.2 Algorithms and Data Structures

Just as a carpenter needs more than a hammer and a
saw to build a house - a programmer will need more
than just an array to develop efficient algorithms. This unit is about the study and implementation of a
wide selection of data structures (the programmers
tools) to enable you to have the correct “tool” for
use in developing efficient algorithms.

## 1.3 Classification of Data Structures 

**There are four types of data structure**

1. Linear Structure

    Contains a collection of nodes (elements) where each node has a **unique predecessor and a unique successor.**

    Examples: Stack, Queue

2. Hierarchical/Tree Structure

    Contains a collection of nodes (elements) where each node has a **unique predecessor and a many successors**.

    Examples: Management Structure, Family Tree
    
3. Network/Graph Structure

    Contains a collection of nodes (elements) where each node has **many predecessors and many successors**.

    Examples: Railway Map, Computer Network

4. Set Structure
    
    Contains a collection of nodes (elements) where each node will have **no predecessors and no successors**.

    Examples: Us students studying this unit

### Activity 1.2

**Explain, in less than ten words, why you will walk twice as far as in one of the towns**

*Town 2 is linear, Town 1 is not.*

Town 2's layout forces backtracking.

In Town 1, the arrangement of houses allows for a continuous path without revisiting any house, minimizing the total distance walked. However, in Town 2, the layout necessitates backtracking, doubling the distance travelled compared to Town 1.

## 1.4 Choosing a Data Structure

### Activity 1.3

**Think of the basic operations that might be performed with a data structure.**

*The fundamental operations that can be performed on a data structure typically include:*

*Insertion: Adding a new data element to the data structure, maintaining its organization and integrity.*

*Deletion: Removing an existing data element from the data structure, ensuring the structure remains consistent after the removal.*

*Searching: Locating a specific data element within the data structure, typically based on a search key or a specific value.*

*Access: Retrieving the value of a particular data element from the data structure, often using an index or a reference.*

*Update: Modifying the value of an existing data element within the data structure, ensuring the updated value is reflected in the structure.*

*Traversal: Visiting each data element in the data structure in a specific order, often to perform an operation on each element or to gather information.*

*Sorting: Arranging the data elements in a specific order, such as ascending or descending order, based on a predefined criteria or comparison function.*

*The specific implementation of these operations varies depending on the type of data structure being used. For example, insertion and deletion in an array may require shifting elements, while in a linked list, it involves modifying pointers. Similarly, searching in a sorted array might use binary search, while in a hash table, it relies on hash functions and key-value pairs.*

*Understanding these basic operations is essential for utilizing data structures effectively in various algorithms and applications. The choice of data structure and the efficiency of its operations significantly impact the performance and resource utilization of software programs.*

## 1.5 Classification of Algorithms

1. Brute Force Algorithm

    Considers all possibilities and selects the best solution

    + simple, should always find the solution as it considers **every** possibility

    - infeasible as the number of possibilities grows exponentially as items increases

2. Divide and Conquer Algorithm

    Divide and conquer algorithms tackle a complex problem by breaking it down into smaller, more manageable subproblems. These subproblems are then solved recursively, meaning the same divide-and-conquer approach is applied to each subproblem until they become simple enough to solve directly. Finally, the solutions to all the subproblems are combined to provide the solution to the original problem.

    Examples: Sorting algorithms, Binary Search Algorithm, Fibonacci Series, more

3. Backtracking Algorithm

    Backtracking algorithms are like a cautious explorer navigating a maze. They build solutions step by step, checking at each step if the current path is still valid. If they reach a dead end, they backtrack to the last valid point and try a different route. This process continues until a complete solution is found or all possibilities are exhausted.

4. Greedy Algorithms

    Greedy algorithms are like a person making decisions based on immediate benefits without considering long-term consequences. They make the best choice at each step, hoping that these local optimal choices will lead to an overall good solution. However, they don't look ahead or reconsider past decisions, so they might miss the best overall solution.

## 1.6 Abstract Data Type (ADT)


In the realm of computer science, an abstract data type (ADT) serves as a conceptual model for data types, defining their behaviour and properties from the user's perspective. It focuses on what the data type can do and what operations it supports, rather than the specific implementation details of how those operations are carried out. ADTs provide a high-level abstraction for data management, allowing programmers to focus on the logical aspects of data manipulation without getting bogged down in low-level implementation details.

An ADT can be thought of as a blueprint or a contract that specifies the behaviour of a data type. It defines the set of operations that can be performed on the data type, the types of values it can hold, and the relationships between those values. However, it doesn't dictate how those operations are implemented or how the data is stored in memory. This separation of concerns allows for flexibility in implementation and promotes code reusability.

**Key characteristics of abstract data types include:**

1. Abstraction: 
    
    ADTs hide the underlying implementation details, allowing programmers to interact with data types at a higher level of abstraction.

2. Encapsulation: 
    
    ADTs encapsulate data and the operations that act on that data, providing a clear boundary between the data representation and its usage.

3.  Specification: 
    
    ADTs are defined by a formal specification that outlines the operations, their behaviour, and the expected outcomes.

4. Implementation 
    
    Independence: ADTs can be implemented using various data structures and algorithms, providing flexibility and adaptability.

5. Modularity: 
    
    ADTs promote modular programming, allowing for independent development and testing of different components.

6. Reusability: 
    
    ADTs can be reused across different applications and contexts, enhancing code efficiency and maintainability.

Abstract data types play a crucial role in software design and development. They provide a clear separation of concerns, promote modularity, and enhance code reusability. By focusing on the logical behaviour of data types, ADTs allow programmers to reason about data manipulation at a higher level, without getting entangled in low-level implementation details. ADTs serve as building blocks for complex data structures and algorithms, fostering a structured and organized approach to software development.

## 1.6.2 Comparison between an ADT and a Data Structure

| Feature | ADT | Data Structure |
|--------|--------|--------|
Focus |	What the data type can do |	How the data is organized and manipulated
Level of Abstraction |	High-level, conceptual model |	Concrete implementation
Purpose |	Defines the behaviour and properties of data |	Manages data efficiently in memory
Implementation |	Independent of specific implementation |	Specific implementation using algorithms and memory allocation
Emphasis |	Logical operations and relationships |	Efficiency and performance of operations

## 1.7 Application - Stack Abstract Data Type

A stack can be best described using **LIFO**.

It is a **Linear Data Structure**.

Can only take the most recent/one off the top item or element. Think about a stack of books.

**A stack must support the following methods**

- Push - Add an element to the top of the stack
- Pop - Remove an element from the top of the stack
- Peek - Examine the element at the top of the stack
- Length - Give the size (number of elements) of the stack

The ADT handles the implementation of the stack. Any application
using the Stack ADT will expect the ADT to throw an exception if:

- Pop or Peek is requested on an empty stack
- Push is requested on a full stack

## 1.7.1 Implementation of a Stack - Using an Array

    class Stack:
    def __init__(self, capacity):
        self.array = [None] * capacity  # Create an empty array
        self.top = -1  # Initialize top index as -1 (empty stack)

    def push(self, item):
        if self.top == len(self.array) - 1:  # Check for overflow
            raise Exception("Stack overflow")
        self.top += 1  # Increment top index
        self.array[self.top] = item  # Add item to the top

    def pop(self):
        if self.top == -1:  # Check for underflow
            raise Exception("Stack underflow")
        item = self.array[self.top]  # Get item from the top
        self.top -= 1  # Decrement top index
        return item  # Return the popped item

    def peek(self):
        if self.top == -1:  # Check for empty stack
            raise Exception("Stack is empty")
        return self.array[self.top]  # Return top element without removing it

    def isEmpty(self):
        return self.top == -1  # True if top index is -1 (empty)

## 1.7.2 Algorithm using the stack ADT - Matching Brackets 

Consider a problem that makes use of the Stack ADT without knowing how it is implemented. The problem is to check that an expression contains the same number of opening and closing brackets. The solution will find the leftmost closed bracket or the rightmost open bracket that is unmatched and indicate its position is the expression.

    function checkBrackets(expression):
        stack = createEmptyStack()
        position = 0  // Track position in expression

        for each character in expression:
          if character is an opening bracket:
            push(stack, character)
          else if character is a closing bracket:
            if stack is empty:
              return position  // Unmatched closing bracket
            else:
              top = pop(stack)
              if top is not the corresponding opening bracket:
                return position  // Unmatched closing bracket
          position = position + 1

        if stack is not empty:
          return position  // Unmatched opening bracket
        else:
          return -1  // All brackets are matched

This algorithm utilizes a stack to keep track of opening brackets. As opening brackets are encountered, they are pushed onto the stack. When a closing bracket is encountered, the corresponding opening bracket is popped from the stack. If the stack is empty or the popped opening bracket doesn't match the closing bracket, an unmatched bracket is found. The position variable keeps track of the location in the expression where the unmatched bracket occurs.

## 1.8 Application - Queue Abstract Data Type

A queue can be best described as **FIFO**.

It is a **Linear Data Structure**.

Elements are inserted into the tail and removed from the head of the queue. Think about literal queues.

**The Queue ADT must support the following methods**

- Enqueue - Add an element to the tail (rear) of the queue
- Dequeue - Remove an element from the head (front) of the queue
- Peek - Examine element at the head of the queue
- Length - Give the size (number) of elements of the queue

## 1.8.1 Implementation of a Queue using an Array (Method 1)

    class Queue:
        def __init__(self, capacity):
            self.Q = [None] * capacity  # Array to store queue elements
            self.head = 0  # Index of the front element
            self.tail = 0  # Index of the last element

        def enqueue(self, item):
            if self.tail == len(self.Q):  # Check for queue overflow
                raise Exception("Queue overflow")

            if self.head == self.tail:
                self.Q[self.tail] = item
                self.tail += 1
            else:
                for i in range(self.tail, 0, -1):  # Shift elements towards the end
                    self.Q[i] = self.Q[i - 1]

                self.Q[0] = item  # Add item at the front
                self.tail += 1

        def dequeue(self):
            if self.head == self.tail:  # Check for empty queue
                raise Exception("Queue underflow")

            item = self.Q[self.head]  # Get item from the front
            self.head += 1

            for i in range(self.head, self.tail):  # Shift elements towards the front
                self.Q[i - 1] = self.Q[i]

            self.tail -= 1
            return item  # Return the dequeued item

In this method, the queue is implemented by shifting elements within the array. When a new element is enqueued, all existing elements are shifted towards the end of the array to make space for the new element at the front. Similarly, when an element is dequeued, all remaining elements are shifted towards the front to fill the gap left by the removed element. This method is straightforward but inefficient due to the constant shifting of elements.

## 1.8.2 Implementation of a Queue using an Array (Method 2)

    class Queue:
        def __init__(self, capacity):
            self.Q = [None] * capacity  # Array to store queue elements
            self.head = 0  # Index of the first empty slot
            self.tail = 0  # Index of the last element

        def enqueue(self, item):
            if self.tail == len(self.Q):  # Check for queue overflow
                raise Exception("Queue overflow")

            self.Q[self.tail] = item  # Add item to the end
            self.tail += 1

        def dequeue(self):
            if self.head == self.tail:  # Check for empty queue
                raise Exception("Queue underflow")

            item = self.Q[self.head]  # Get item from the front
            self.head += 1
            return item  # Return the dequeued item

In this method, the queue is implemented by leaving empty spaces in the array. New elements are enqueued at the end of the array, and the tail pointer is incremented. However, the dequeue operation only increments the head pointer, leaving empty spaces between the head and tail. This method avoids element shifting but wastes space as the array fills up with empty slots.


## 1.8.3 Implementation of a Queue using an Array (Method 3)

    class Queue:

        def __init__(self, capacity):
            self.Q = [None] * capacity  # Array to store queue elements
            self.head = 0  # Index of the front element
            self.tail = 0  # Index of the next available slot

        def enqueue(self, item):
            if self.isFull():  # Check for queue overflow
                raise Exception("Queue overflow")
            self.Q[self.tail] = item  # Add item to the end
            self.tail = (self.tail + 1) % len(self.Q)  # Increment tail with wraparound

        def dequeue(self):
            if self.isEmpty():  # Check for empty queue
                raise Exception("Queue underflow")
            item = self.Q[self.head]  # Get item from the front
            self.head = (self.head + 1) % len(self.Q)  # Increment head with wraparound
            return item  # Return the dequeued item

        def isEmpty(self):
            return self.head == self.tail  # True if head and tail are equal

        def isFull(self):
            return (self.tail + 1) % len(self.Q) == self.head  # True if tail is one behind head

In this method, the queue is implemented using a circular array, where the head and tail pointers wrap around to the beginning of the array when they reach the end. New elements are enqueued at the end, and the tail pointer is incremented with wraparound. Dequeued elements are removed from the front, and the head pointer is incremented with wraparound. This method efficiently utilizes the entire array without wasting space or requiring element shifting.

### Activity 1.4

**To remove the last element from a circular queue - i.e. after the deletion the queue will become empty.**

*There will be an overflow/underflow error in trying to insert into a full queue or remove from an empty queue*

*Head is tail + 1*

*As the queue will only become full/empty after the operation is performed, there needs to be a catch before that is executed, like maintaining an empty space within the array*