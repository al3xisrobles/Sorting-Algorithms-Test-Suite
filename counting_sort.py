class CountingSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        max_num = max(arr)
        min_num = min(arr)
        k = max_num - min_num + 1
        counts = [0] * k

        # Create array (dictionary) for frequencies
        for num in arr:
            counts[num - min_num] += 1

        # Turn counts into prefix sum
        for i in range(len(counts) - 1):
            counts[i + 1] = counts[i + 1] + counts[i]

        # Put elements into their respective locations
        arr_sorted = [None] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            arr_sorted[counts[arr[i] - min_num] - 1] = arr[i]
            counts[arr[i] - min_num] -= 1

        return arr_sorted
