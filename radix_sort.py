class RadixSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        # Get the maximum number to know the number of digits
        max_num = max(arr)

        # Initialize the exponent to 1 (for the least significant digit)
        exp = 1

        # Continue until we have processed all digits
        while max_num // exp > 0:
            self.counting_sort_digits(arr, exp)
            exp *= 10

        return arr

    def counting_sort_digits(self, arr, exp):
        n = len(arr)

        # Initialize output array and count array
        output = [0] * n
        count = [0] * 10  # Since the base is 10

        # Store count of occurrences in count[]
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Change count[i] so that count[i] contains the actual position of
        # this digit in the output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        # Copy the output array to arr[], so that arr now
        # contains sorted numbers according to current digit
        for i in range(n):
            arr[i] = output[i]
