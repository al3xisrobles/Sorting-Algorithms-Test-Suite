import unittest
import random
from termcolor import colored
from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from heap_sort import HeapSort
from bucket_sort import BucketSort
from radix_sort import RadixSort
from counting_sort import CountingSort
from bitmap_sort import BitmapSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        random_test_case = random.sample(range(10000), 1000)
        self.test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 3, 2], [1, 2, 3]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([3, 3, 1], [1, 3, 3]),
            ([9, 7, 5, 3, 1, 2, 4, 6, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            (random_test_case, sorted(random_test_case))
        ]

        self.algorithms = [
            BubbleSort(),
            SelectionSort(),
            InsertionSort(),
            MergeSort(),
            QuickSort(),
            HeapSort(),
            BucketSort(),
            RadixSort(),
            CountingSort(),
            BitmapSort()
        ]

    def truncate_arr(self, arr):
        if len(arr) <= 30:
            return str(arr)
        return str(arr[:30]).replace("]", ", ...]")

    def test_sorting_algorithms(self):
        print("Enter the number of the algorithm you want to test:")
        for index, algorithm in enumerate(self.algorithms):
            print(f"{index + 1}. {algorithm.__class__.__name__.replace('Sort', ' Sort')}")

        # Get algorithm
        idx = int(input("\n"))
        algorithm = self.algorithms[idx - 1]
        print(f"\nTesting {algorithm.__class__.__name__.replace('Sort', ' Sort')}...")

        # Run tests
        with self.subTest(algorithm=algorithm.__class__.__name__):
            for input_arr, expected in self.test_cases:
                result = algorithm.sort(input_arr.copy())
                try:
                    self.assertEqual(result, expected)
                    print(colored(f"Passed {algorithm.__class__.__name__} with input {self.truncate_arr(input_arr)}", "green"))
                except AssertionError as e:
                    print(colored(f"Failed {algorithm.__class__.__name__} with input {self.truncate_arr(input_arr)}", "red"))
if __name__ == "__main__":
    unittest.main()
