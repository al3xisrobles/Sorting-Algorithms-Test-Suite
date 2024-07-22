class QuickSelect:
    def quickselect(self, arr, k):
        if not arr or k > len(arr):
            return None
        if len(arr) == 1:
            return arr[0]

        def place_pivot(arr, start, end):
            """Places the pivot in its correct position in the subarray, with
            items on the left being < its value and those on the right being >"""
            right_start_idx = start
            pivot_idx = end

            for i in range(start, end):
                if arr[i] < arr[pivot_idx]:
                    arr[i], arr[right_start_idx] = arr[right_start_idx], arr[i]
                    right_start_idx += 1

            arr[right_start_idx], arr[pivot_idx] = arr[pivot_idx], arr[right_start_idx]
            return right_start_idx

        start, end = 0, len(arr) - 1
        while start <= end:
            pivot_idx = place_pivot(arr, start, end)
            if pivot_idx == k:
                return arr[pivot_idx]
            if pivot_idx < k:
                start = pivot_idx + 1
            else:
                end = pivot_idx - 1










import unittest
from termcolor import colored
class TestQuickSelect(unittest.TestCase):
    def setUp(self):
        self.algorithm = QuickSelect()

    def truncate_arr(self, arr):
        if len(arr) <= 30:
            return str(arr)
        return str(arr[:30]).replace("]", ", ...]")

    def test_quickselect(self):
        print("\nTesting QuickSelect...")
        test_cases = [
            ([3, 2, 1, 5, 4], 1, 2),
            ([3, 2, 1, 5, 4], 3, 4),
            ([1], 0, 1),
            ([7, 10, 4, 3, 20, 15], 3, 10),
            ([7, 10, 4, 3, 20, 15], 4, 15),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 9),
        ]

        for input_arr, k, expected in test_cases:
            result = self.algorithm.quickselect(input_arr.copy(), k)
            try:
                self.assertEqual(result, expected)
                print(colored(f"Passed QuickSelect with input {self.truncate_arr(input_arr)} and k={k}", "green"))
            except AssertionError as e:
                print(colored(f"Failed QuickSelect with input {self.truncate_arr(input_arr)} and k={k}", "red"))

if __name__ == "__main__":
    unittest.main()
