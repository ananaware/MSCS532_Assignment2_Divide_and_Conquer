"""
quick_sort.py
MSCS532 Assignment 2 - Divide-and-Conquer Algorithms

Quick Sort implementation (choose pivot, partition, sort recursively).
"""

from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition the array into elements <= pivot and > pivot.
    Returns the index of the pivot after partitioning.
    """
    pivot = arr[high]  # choose last element as pivot
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
    Time complexity: best/average Θ(n log n), worst Θ(n^2)
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def quick_sort_wrapper(arr: List[int]) -> List[int]:
    """
    Wrapper to make quick_sort return a new list (instead of in-place modification).
    """
    copy = arr[:]  # work on a copy
    quick_sort(copy, 0, len(copy) - 1)
    return copy


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted:  ", quick_sort_wrapper(sample))
