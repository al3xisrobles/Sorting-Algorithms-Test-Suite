class HeapSort:
    def sort(self, arr):
        n = len(arr)

        def max_heapify(subarray, last_idx, i):
            if i > last_idx:
                return

            l_idx = i * 2 + 1
            r_idx = i * 2 + 2

            largest = i

            if l_idx < last_idx and subarray[l_idx] > subarray[largest]:
                largest = l_idx

            if r_idx < last_idx and subarray[r_idx] > subarray[largest]:
                largest = r_idx

            if largest != i:
                subarray[i], subarray[largest] = subarray[largest], subarray[i]
                max_heapify(subarray, last_idx, largest)

        # Build the max heap
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(arr, n, i)

        # Repeatedly swap max for the last position until 1 element
        for last_idx in range(n - 1, -1, -1):
            # Move max element to the sorted side, swapping out with smallest
            arr[0], arr[last_idx] = arr[last_idx], arr[0]

            # Bubble down smallest element to keep max-heap invariant
            max_heapify(arr, last_idx, 0)

        return arr
