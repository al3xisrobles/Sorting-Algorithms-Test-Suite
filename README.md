# SortingAlgos

A testing suite and (completed) implementation template for the most common sorting algorithms. These include:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Bucket Sort
8. Radix Sort
9. Counting Sort
10. Bitmap Sort

Also includes Quick Select, a selection algorithm similar to quicksort.

### Steps to run:

Clone this directory:
```
git clone https://github.com/al3xisrobles/SortingAlgos.git
```

In the directory created, create a virtual python environment
```
python3 -m venv venv
```

Activate the environment
```
source venv/bin/activate
```

Run the testing suite (excludes quickselect)
```
python3 test.py
```

If you want to test quickselect, run that separate test case with
```
python3 quick_select.py
```
