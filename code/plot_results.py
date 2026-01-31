"""
plot_results.py
MSCS532 Assignment 2 - Divide-and-Conquer Algorithms

Generate performance graphs from benchmark results.
"""

import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def load_results(filename: str):
    """
    Load benchmark results from CSV.
    """
    data = defaultdict(lambda: defaultdict(list))

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            algorithm = row["algorithm"]
            data_type = row["data_type"]
            size = int(row["size"])
            time_sec = float(row["time_seconds"])

            data[(algorithm, data_type)]["sizes"].append(size)
            data[(algorithm, data_type)]["times"].append(time_sec)

    return data


def plot_results(data):
    """
    Generate line plots for each dataset type.
    """
    for data_type in ["sorted", "reverse", "random"]:
        plt.figure()

        for algorithm in ["Merge Sort", "Quick Sort"]:
            key = (algorithm, data_type)
            plt.plot(
                data[key]["sizes"],
                data[key]["times"],
                marker="o",
                label=algorithm,
            )

        plt.xlabel("Input Size (n)")
        plt.ylabel("Execution Time (seconds)")
        plt.title(f"Performance on {data_type.capitalize()} Data")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{data_type}_performance.png")
        plt.close()


if __name__ == "__main__":
    results = load_results("results.csv")
    plot_results(results)
    print("Graphs generated successfully.")
