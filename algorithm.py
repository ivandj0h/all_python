# Bubble sort and Insertion sort –
# Average and worst case time complexity: n^2
# Best case time complexity: n when array is already sorted.
# Worst case: when the array is reverse sorted.

# Selection sort –
# Best, average and worst case time complexity: n^2 which is independent of distribution of data.

# Merge sort –
# Best, average and worst case time complexity: nlogn which is independent of distribution of data.

# Heap sort –
# Best, average and worst case time complexity: nlogn which is independent of distribution of data.

# Quick sort –
# It is a divide and conquer approach with recurrence relation:

#  T(n) = T(k) + T(n-k-1) + cn
# Worst case: when the array is sorted or reverse sorted, the partition algorithm divides the array in two subarrays with 0 and n-1 elements. Therefore,

# T(n) = T(0) + T(n-1) + cn
# Solving this we get, T(n) = O(n^2)
# Best case and Average case: On an average, the partition algorithm divides the array in two subarrays with equal size. Therefore,

# T(n) = 2T(n/2) + cn
# Solving this we get, T(n) = O(nlogn)
# Non-comparison based sorting –
# In non-comparison based sorting, elements of array are not compared with each other to find the sorted array.


# Radix sort –
# Best, average and worst case time complexity: nk where k is the maximum number of digits in elements of array.

# Count sort –
# Best, average and worst case time complexity: n+k where k is the size of count array.

# Bucket sort –
# Best and average time complexity: n+k where k is the number of buckets.
# Worst case time complexity: n^2 if all elements belong to same bucket.

# https://www.interviewzen.com/interview/05ac66c9-ede2-42d6-a3ef-6232d52d2dd2
