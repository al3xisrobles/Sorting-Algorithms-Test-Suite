class InsertionSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        for sorted_idx in range(len(arr) - 1):
            candidate = arr[sorted_idx + 1]

            # Move everything up one while looking for correct spot
            insertion_idx = sorted_idx
            while insertion_idx >= 0 and candidate < arr[insertion_idx]:
                arr[insertion_idx + 1] = arr[insertion_idx]
                insertion_idx -= 1

            # Insert the number into its correct position in the sorted section
            arr[insertion_idx + 1] = candidate

        return arr
