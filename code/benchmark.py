"""
benchmark.py
MSCS532 Assignment 2 - Divide-and-Conquer Algorithms

Benchmark Merge Sort and Quick Sort on multiple datasets and record execution time.
"""

import time
import random
import csv

from merge_sort import merge_sort
from quick_sort import quick_sort_wrapper


def generate_data(size: int) -> dict[str, list[int]]:
    """
    Generate sorted, reverse sorted, and random lists of given size.
    """
    sorted_list = list(range(size))
    reverse_list = sorted_list[::-1]
    random_list = random.sample(range(size * 2), size)

    return {
        "sorted": sorted_list,
        "reverse": reverse_list,
        "random": random_list,
    }


def time_function(func, arr: list[int]) -> float:
    """
    Time how long func(arr) takes, returning time in seconds.
    """
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start


def benchmark():
    """
    Run benchmarks on lists of different sizes.
    Record results to 'results.csv'.
    """
    sizes = [500, 1000, 2000, 5000, 10000]
    header = ["algorithm", "data_type", "size", "time_seconds"]

    with open("results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for size in sizes:
            data_sets = generate_data(size)

            for data_type, dataset in data_sets.items():
                # Time Merge Sort
                merge_time = time_function(merge_sort, dataset)
                writer.writerow(["Merge Sort", data_type, size, merge_time])

                # Time Quick Sort
                quick_time = time_function(quick_sort_wrapper, dataset)
                writer.writerow(["Quick Sort", data_type, size, quick_time])

    print("Benchmarking complete. Results saved to results.csv.")


if __name__ == "__main__":
    benchmark()
