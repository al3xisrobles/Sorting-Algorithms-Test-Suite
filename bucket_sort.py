import math

class BucketSort:
    def sort(self, arr):
        if len(arr) < 2:
            return arr

        # Create arbitrary number of buckets
        n_buckets = len(arr)
        buckets = [[] for _ in range(n_buckets)]

        # Place each element from the input array into each bucket
        max_num = max(arr)
        min_num = min(arr)
        elements_in_each_bucket = math.ceil((max_num - min_num) / n_buckets)
        for num in arr:
            bucket_idx = (num - min_num) // elements_in_each_bucket
            buckets[bucket_idx].append(num)

        # Sort each bucket
        for bucket in buckets:
            bucket.sort()

        # Combine all buckets
        sorted = []
        for bucket in buckets:
            sorted.extend(bucket)

        return sorted
