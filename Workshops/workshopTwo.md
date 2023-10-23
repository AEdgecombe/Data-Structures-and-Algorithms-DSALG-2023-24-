# Workshop 2 - Tools of the Trade: Part 1 - Complexity of Algorithms

## 2.1 Efficiency of Algorithms

When comparing different algorithms to solve the same problem, often one algorithm will be much more efficient than another algorithm, thus we need to be able to recognise and choose the more efficient algorithm.

If an algorithm contains no loops, then its efficiency is a function of the number of instructions it contains i.e. its efficiency is dependent on the speed of the computer. 

Algorithms consisting of loops vary in their efficiency depending on how the loops handle the data. Hence the study of algorithm efficiency is mainly linked to the study of loops. The amount of data to be processed and how it is ordered can also affect the speed of your algorithm. For example: consider a sorting algorithm - the algorithm may (or may not) run quicker if the data is already sorted compared to the same data presented in a random order.

**Example**

Consider the following three different algorithms to evaluate the series:

```
1 + 2 + 3 + 4 +...+ n
```
for any positive integer n

**Algorithm A**

```
sum = 0
for J = 1 to N loop
    sum = sum + J
end loop
```

**Algorithm B**

```
sum = 0
for J = 1 to N loop
    for K = 1 to J loop
        sum = sum + 1
    end loop
end loop
```

**Algorithm C**

```
sum = N * (N + 1) /2
```

**We need to determine which algorithm is the most efficient.**

The following table shows the total number of operations for each algorithm:


| Operation | Algorithm A | Algorithm B | Algorithm C |
|---|---|---|---|
| Assignment | N+1 | 1 + N* (N + 1)/2 | 1 |
| Additions | N | N*(N+1)/2 | 1 |
| Multiplication | 0 | 0 | 1 |
| Division | 0 | 0 | 1 |
| Total Operations | 2N + 1 | N²+N+1 | 4 |

**From this table we can observe:**

* Algorithm A requires - time proportional to 2N + 1
* Algorithm B requires - time proportional to N²+ N + 1
* Algorithm C requires - constant time that is independent of N

**Hence we can determine that:**

* Algorithm B requires the most time.
* Algorithm C requires the least time and is thus the most efficient.

## 2.2 Growth Rate of Functions

The example in the previous section calculated a precise measurement of the efficiency of each algorithm. Normally we are only interested in the general efficiency of an algorithm.

The following table shows the growth rate of several functions:

| N | log₂N | N log N | N² | 2^N |
|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 2 |
| 2 | 1 | 2 | 4 | 4 |
| 4 | 2 | 8 | 16 | 16 |
| 8 | 3 | 24 | 64 | 256 |
| 16 | 4 | 64 | 256 | 65,536 |
| 32 | 5 | 160 | 1,024 | 4,294,967,296 |

Sure, here is the markdown notes for the text:

## 2.3.1. Using Big O notation

Revisiting the three algorithms from section 2.1, we can represent their general efficiency using Big O notation:

**Algorithm A:**

- Time proportional to 2N + 1
- N has a more significant effect on efficiency than 1
- Big O notation: O(N)
- Efficiency: Linear - dependent on N

**Algorithm B:**

- Time proportional to N^2 + N + 1
- N^2 has a more significant effect on efficiency than N or 1
- Big O notation: O(N^2)
- Efficiency: Quadratic - dependent on N^2

**Algorithm C:**

- Time is constant and independent of N
- Efficiency remains constant regardless of N
- Big O notation: O(1)
- Efficiency: Constant - independent of N


