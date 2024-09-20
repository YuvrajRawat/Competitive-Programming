# Reverse an Array/String

# n = "yuvraj"

# def reverse(n):
#     new = n[::-1]

#     return new

# result = reverse(n)
# print(result)

# Find the maximum and minimum element in an array

# n = [1,2,3,67,54,4]

# def max_min(n):

#     n.sort()

#     return n[0],n[-1]

# result = max_min(n)
# print(result)

# Find the “Kth” max and min element of an array

# n = [1,2,3,67,54,4]
# k = 2

# def max_min(n,k):

#     n.sort()

#     return n[k-1],n[-k]

# result = max_min(n,k)
# print(result)

# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# Move all the negative elements to one side of the array
# Find the Union and Intersection of the two sorted arrays.

# n = [1,2,3,67,54,4]
# m = [3,4,5,6,94,43]

# def u_i(n,m):
#     x = n + m
#     y = []

#     for i in range(len(n)):
#         for j in range(len(m)):
#             if n[i] == m[j]:
#                 y.append(n[i])
    
#     return f"the unionis {x} and the intersection is {y}"

# result = u_i(n,m)
# print(result)

# Write a program to cyclically rotate an array by one.

# def cycle(arr):
#     if not arr:  # Check if the array is empty
#         return arr
#     return [arr[-1]] + arr[:-1]

# n = [1, 2, 3, 4, 5]
# result = cycle(n)
# print(result)

# Find Largest sum contiguous Subarray [V. IMP]

# Minimize the maximum difference between heights [V.IMP]
# Minimum no. of Jumps to reach end of an array
# Find duplicate in an array of N+1 Integers
# Merge 2 sorted arrays without using Extra space.
# Kadane’s Algo [V.V.V.V.V IMP]
# Merge Intervals
# Next Permutation
# Count Inversion
# Best time to buy and Sell stock
# Find all pairs on integer array whose sum is equal to given number
# Find common elements In 3 sorted arrays
# def common(n1,n2,n3):
#     common = []
#     for i in range(len(n1)):
#         for j in range(len(n2)):
#             for k in range(len(n3)):
#                 if n1[i] == n2[j] == n3[k]:
#                     common.append(n1[i])
#     return common

# n1 = [1, 2, 3, 4, 5]
# n2 = [4, 5, 6, 7, 8]
# n3 = [5, 6, 7, 8, 9]

# result = common(n1,n2,n3)
# print(result)

# Rearrange the array in alternating positive and negative items with O(1) extra space
# Find if there is any subarray with sum equal to 0
# Find factorial of a large number
# Find maximum product subarray
# Find longest consecutive subsequence
# Given an array of size n and a number k, fin all elements that appear more than ” n/k ” times.
# Maximum profit by buying and selling a share at most twice
# Find whether an array is a subset of another array
# Find the triplet that sum to a given value
# Trapping Rain water problem
# Chocolate Distribution problem
# Smallest Subarray with sum greater than a given value
# Three way partitioning of an array around a given value
# Minimum swaps required bring elements less equal K together
# Minimum no. of operations required to make an array palindrome
# Median of 2 sorted arrays of equal size
# Median of 2 sorted arrays of different size

# Spiral traversal on a Matrix
# Search an element in a Matrix
# Find median in a row wise sorted matrix
# Find row with maximum no. of 1’s
# Print elements in sorted order using row-column wise sorted matrix
# Maximum size rectangle
# Find a specific pair in matrix
# Rotate matrix by 90 degrees
# Kth smallest element in a row-column wise sorted matrix
# Common elements in all rows of a given matrix

# Reverse a String
# Check whether a String is Palindrome or not
# Find Duplicate characters in a string
# Why strings are immutable in Java?
# Write a Code to check whether one string is a rotation of another
# Write a Program to check whether a string is a valid shuffle of two strings or not
# Count and Say problem
# Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]
# Find Longest Recurring Subsequence in String
# Print all Subsequences of a string.
# Print all the permutations of the given string
# Split the Binary string into two substring with equal 0’s and 1’s
# Word Wrap Problem [VERY IMP].
# EDIT Distance [Very Imp]
# Find next greater number with same set of digits. [Very Very IMP]
# Balanced Parenthesis problem.[Imp]
# Word break Problem[ Very Imp]
# Rabin Karp Algorithm
# KMP Algorithm
# Convert a Sentence into its equivalent mobile numeric keypad sequence.
# Minimum number of bracket reversals needed to make an expression balanced.
# Count All Palindromic Subsequence in a given String.
# Count of number of given string in 2D character array
# Search a Word in a 2D Grid of characters.
# Boyer Moore Algorithm for Pattern Searching.
# Converting Roman Numerals to Decimal
# Longest Common Prefix
# Number of flips to make binary string alternate
# Find the first repeated word in string.
# Minimum number of swaps for bracket balancing.
# Find the longest common subsequence between two strings.
# Program to generate all possible valid IP addresses from given  string.
# Write a program to find the smallest window that contains all characters of string itself.
# Rearrange characters in a string such that no two adjacent are same
# Minimum characters to be added at front to make string palindrome
# Given a sequence of words, print all anagrams together
# Find the smallest window in a string containing all characters of another string
# Recursively remove all adjacent duplicates
# String matching where one string contains wildcard characters
# Function to find Number of customers who could not get a computer
# Transform One String to Another using Minimum Number of Given Operation
# Check if two given strings are isomorphic to each other
# Recursively print all sentences that can be formed from list of word lists

# Find first and last positions of an element in a sorted array
# Find a Fixed Point (Value equal to index) in a given array
# Search in a rotated sorted array
# Square root of an integer
# Maximum and minimum of an array using minimum number of comparisons
# Optimum location of point to minimize total distance
# Find the repeating and the missing
# Find majority element
# Searching in an array where adjacent differ by at most k
# Find a pair with a given difference
# Find four elements that sum to a given value
# Maximum sum such that no 2 elements are adjacent
# Count triplet with sum smaller than a given value
# Merge 2 sorted arrays
# Product array Puzzle
# Sort array according to count of set bits
# Minimum no. of swaps required to sort the array
# Bishu and Soldiers
# Rasta and Kheshtak
# Kth smallest number again
# Find pivot element in a sorted array
# K-th Element of Two Sorted Arrays
# Aggressive cows
# Book Allocation Problem
# EKOSPOJ:
# Job Scheduling Algo
# Missing Number in AP
# Smallest number with atleast n trailing zeroes in factorial
# Painters Partition Problem:
# ROTI-Prata SPOJ
# DoubleHelix SPOJ
# Subset Sums
# Find the inversion count
# Implement Merge-sort in-place
# Partitioning and Sorting Arrays with Many Repeated Entries

# Write a Program to reverse the Linked List. (Both Iterative and recursive)
# Reverse a Linked List in group of Given Size. [Very Imp]
# Write a program to Detect loop in a linked list.
# Write a program to Delete loop in a linked list.
# Find the starting point of the loop.
# Remove Duplicates in a sorted Linked List.
# Remove Duplicates in a Un-sorted Linked List.
# Write a Program to Move the last element to Front in a Linked List.
# Add “1” to a number represented as a Linked List.
# Add two numbers represented by linked lists.
# Intersection of two Sorted Linked List.
# Intersection Point of two Linked Lists.
# Merge Sort For Linked lists.[Very Important]
# Quicksort for Linked Lists.[Very Important]
# Find the middle Element of a linked list.
# Check if a linked list is a circular linked list.
# Split a Circular linked list into two halves.
# Write a Program to check whether the Singly Linked list is a palindrome or not.
# Deletion from a Circular Linked List.
# Reverse a Doubly Linked list.
# Find pairs with a given sum in a DLL.
# Count triplets in a sorted DLL whose sum is equal to given value “X”.
# Sort a “k”sorted Doubly Linked list.[Very IMP]
# Rotate Doubly Linked list by N nodes.
# Rotate a Doubly Linked list in group of Given Size.[Very IMP]
# Can we reverse a linked list in less than O(n) ?
# Why Quicksort is preferred for. Arrays and Merge Sort for Linked Lists ?
# Flatten a Linked List
# Sort a LL of 0’s, 1’s and 2’s
# Clone a linked list with next and random pointer
# Merge K sorted Linked list
# Multiply 2 no. represented by LL
# Delete nodes which have a greater value on right side
# Segregate even and odd nodes in a Linked List
# Program for n’th node from the end of a Linked List

# Count set bits in an integer
# Find the two non-repeating elements in an array of repeating elements
# Count number of bits to be flipped to convert A to B
# Count total set bits in all numbers from 1 to n
# Program to find whether a no is power of two
# Find position of the only set bit
# Copy set bits in a range
# Divide two integers without using multiplication, division and mod operator
# Calculate square of a number without using *, / and pow()
# Power Set

