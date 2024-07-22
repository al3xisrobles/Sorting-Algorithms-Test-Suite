class BitmapSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        max_num = max(arr)
        min_num = min(arr)
        bitmap = [0] * (max_num - min_num + 1)

        for num in arr:
            bitmap[num - min_num] = 1

        output = []
        for i, bit in enumerate(bitmap):
            if bit:
                output.append(i + min_num)

        return output

# MAY FAIL FOR NON-DISTINCT INPUT ARRAYS. Bitmap sort assumes all input elements
# are distinct.
