"""
merge_sort.py
MSCS532 Assignment 2 - Divide-and-Conquer Algorithms

Merge Sort implementation (divide array into halves, sort recursively, merge).
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr: List[int]) -> List[int]:
    """
    Return a new sorted list using Merge Sort.
    Time complexity: Θ(n log n)
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted:  ", merge_sort(sample))
