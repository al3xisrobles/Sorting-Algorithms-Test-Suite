class BubbleSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        for window in range(len(arr) - 1, -1, -1):
            swapped = False
            for i in range(window):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break

        return arr
