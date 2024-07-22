class MergeSort:
    def sort(self, arr):
        def merge(left, mid, right):
            left_copy = arr[left:mid+1]
            right_copy = arr[mid+1:right+1]

            l_idx = r_idx = 0
            arr_idx = left

            while l_idx < len(left_copy) and r_idx < len(right_copy):
                if left_copy[l_idx] < right_copy[r_idx]:
                    arr[arr_idx] = left_copy[l_idx]
                    l_idx += 1
                else:
                    arr[arr_idx] = right_copy[r_idx]
                    r_idx += 1
                arr_idx += 1

            while l_idx < len(left_copy):
                arr[arr_idx] = left_copy[l_idx]
                l_idx += 1
                arr_idx += 1
            while r_idx < len(right_copy):
                arr[arr_idx] = right_copy[r_idx]
                r_idx += 1
                arr_idx += 1

        def mergeSort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            merge(left, mid, right)

        mergeSort(0, len(arr) - 1)
        return arr
