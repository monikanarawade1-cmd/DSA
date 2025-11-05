Read the marks obtained by students of second year in an online examination of particular subject. Find out maximum and minimum marks obtained in a that subject. Use heap data structure. Analyze the algorithm. 

import heapq

# Read marks
marks = list(map(int, input("Enter marks separated by space: ").split()))

# Create min-heap
min_heap = marks[:]
heapq.heapify(min_heap)
min_mark = min_heap[0]

# Create max-heap by pushing negative marks
max_heap = [-m for m in marks]
heapq.heapify(max_heap)
max_mark = -max_heap[0]

print(f"Minimum mark: {min_mark}")
print(f"Maximum mark: {max_mark}")


OUTPUT:
Enter marks separated by space: 56 78 89 34 67 90
Minimum mark: 34
Maximum mark: 90

