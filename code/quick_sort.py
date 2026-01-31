"""
quick_sort.py
MSCS532 Assignment 2 - Divide-and-Conquer Algorithms

Quick Sort implementation using randomized pivot selection.
"""

import random
from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition using a randomized pivot to avoid worst-case recursion.
    """
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    In-place Quick Sort.
    Best/Average: Θ(n log n)
    Worst: Θ(n^2)
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def quick_sort_wrapper(arr: List[int]) -> List[int]:
    """
    Wrapper to return a new sorted list for benchmarking consistency.
    """
    copy = arr[:]
    if len(copy) > 0:
        quick_sort(copy, 0, len(copy) - 1)
    return copy


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted:  ", quick_sort_wrapper(sample))
