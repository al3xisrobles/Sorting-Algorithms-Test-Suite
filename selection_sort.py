class SelectionSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        # Iterate through the whole array,
        for unsorted_idx in range(1, len(arr)):
            sorted_idx = unsorted_idx - 1

            smallest = float('inf')
            smallest_idx = None
            for i in range(sorted_idx, len(arr)):
                if arr[i] < smallest:
                    smallest = arr[i]
                    smallest_idx = i

            # If the smallest of the unsorted is still larger, we don't swap
            if smallest > arr[unsorted_idx]:
                continue

            # Swap
            arr[smallest_idx], arr[sorted_idx] = arr[sorted_idx], arr[smallest_idx]

        return arr
