class QuickSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        def place_pivot(arr, start, end):
            """Places the pivot in its correct position in the subarray, with
            items on the left being < its value and those on the right being >"""
            right_start_idx = start
            pivot_idx = end

            #
            for i in range(start, end):
                if arr[i] < arr[pivot_idx]:
                    arr[i], arr[right_start_idx] = arr[right_start_idx], arr[i]
                    right_start_idx += 1

            arr[right_start_idx], arr[pivot_idx] = arr[pivot_idx], arr[right_start_idx]
            return right_start_idx

        def quicksort(arr, start, end):
            """Helper function to recursively call itself with start and end values"""
            if start >= end:
                return

            pivot_idx = place_pivot(arr, start, end)

            quicksort(arr, start, pivot_idx - 1)
            quicksort(arr, pivot_idx + 1, end)

        quicksort(arr, 0, len(arr) - 1)
        return arr
