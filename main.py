import random
from timeit import default_timer as timer
import numpy as np
import sys


def partitionDeterministic(low, high, array):
    # Initializing pivot's index to start
    pivot_index = low
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while low < high:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while low < len(array) and array[low] <= pivot:
            low += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[high] > pivot:
            high -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if low < high:
            array[low], array[high] = array[high], array[low]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[high], array[pivot_index] = array[pivot_index], array[high]

    # Returning end pointer to divide the array into 2
    return high


# The main function that implements Deterministic QuickSort
def quick_sort(low, high, array):
    if low < high:
        # p is partitioning index, array[p]
        # is at right place
        p = partitionDeterministic(low, high, array)

        # Sort elements before partition
        # and after partition
        quick_sort(low, p - 1, array)
        quick_sort(p + 1, high, array)

# partition for median of three quicksort
def partition(array, lowest, highest):
    pivot = median_of_three(array, lowest, highest)
    x = lowest - 1
    y = highest + 1
    while True:
        x += 1
        while array[x] < pivot:
            x += 1
        y -= 1
        while array[y] > pivot:
            y -= 1
        if x >= y:
            return y
        array[x], array[y] = array[y], array[y]


def median_of_three(array, lowest, highest):
    middle = (lowest + highest - 1) // 2
    if (array[lowest] - array[middle]) * (array[highest] - array[lowest]) >= 0:
        return array[lowest]
    elif (array[middle] - array[lowest]) * (array[highest] - array[middle]) >= 0:
        return array[middle]
    else:
        return array[highest]


# quicksort for median of three
def quickSort(array, lowest, highest):
    if highest is None:
        highest = len(array) - 1

    if lowest < highest:
        p = partition(array, lowest, highest)
        quickSort(array, lowest, p)
        quickSort(array, p + 1, highest)


# randomized quicksort
def quickSortRandom(array, low, high):
    if low < high:
        pivotPoint = partitionRandom(array, low, high)
        quickSortRandom(array, low, pivotPoint - 1)
        quickSortRandom(array, pivotPoint + 1, high)


# partition for randomized quicksort
def partitionRandom(array, low, high):
    r = random.randrange(low, high)

    array[low], array[r] = array[r], array[low]

    pivotItem = array[low]

    j = low
    for i in range(low + 1, high + 1):
        if array[i] < pivotItem:
            j = j + 1
            array[i], array[j] = array[j], array[i]

    pivotPoint = j
    array[low], array[pivotPoint] = array[pivotPoint], array[low]
    return pivotPoint


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 8)
    # experiments 1
    time = []
    time1 = []
    time6 = []
    for i in range(1, 11):
        n = 1000 * i
        array1 = []
        for j in range(n, 0, -1):
            array1.append(j)

        start = timer()
        quickSortRandom(array1, 0, len(array1) - 1)
        end = timer()
        time.append((end - start) * 1000000)  # microseconds

        start = timer()
        quickSort(array1, 0, len(array1) - 1)
        end = timer()
        time1.append((end - start) * 1000000)

        start = timer()
        quick_sort(0, len(array1) - 1, array1)
        end = timer()
        time6.append((end - start) * 1000000)

    # experiments 2
    time2 = []
    time4 = []
    time7 = []
    i = 0
    j = 0
    for i in range(1, 11):
        n = 1000 * i
        array1 = []
        for j in range(1, n + 1):
            array1.append(j)

        # swap ten pairs
        for k in range(0, 11):
            r1 = random.randrange(0, n + 1)
            r2 = random.randrange(0, n + 1)

            array1[r1], array1[r2] = array1[r2], array1[r1]

        start = timer()
        quickSortRandom(array1, 0, len(array1) - 1)
        end = timer()
        time2.append((end - start) * 1000000)  # microseconds

        start = timer()
        quickSort(array1, 0, len(array1) - 1)
        end = timer()
        time4.append((end - start) * 1000000)

        start = timer()
        quick_sort(0, len(array1) - 1, array1)
        end = timer()
        time7.append((end - start) * 1000000)

    # experiments 3
    time3 = []
    time5 = []
    time8 = []
    i = 0
    j = 0
    for i in range(1, 11):
        sumTime = 0
        sumTime2 = 0
        sumTime3 = 0
        n = 1000 * i
        for j in range(0, 11):
            array1 = []

            for j in range(1, n + 1):
                array1.append(j)

            array2 = np.random.permutation(array1)
            start = timer()
            quickSortRandom(array2, 0, len(array2) - 1)
            end = timer()
            sumTime = sumTime + ((end - start) * 1000000)

            start = timer()
            quickSort(array1, 0, len(array1) - 1)
            end = timer()
            sumTime2 = sumTime2 + ((end - start) * 1000000)

            start = timer()
            quick_sort(0, len(array1) - 1, array1)
            end = timer()
            sumTime3 = sumTime3 + ((end - start) * 1000000)

        time3.append(sumTime / 10)
        time5.append(sumTime2 / 10)
        time8.append(sumTime3 / 10)

    print("Random quicksort experiments:")

    print("Experiment 1: ", time)
    print("Experiment 2: ", time2)
    print("Experiment 3: ", time3)

    print("Median of three experiments:")
    print("Experiment 1: ", time1)
    print("Experiment 2: ", time4)
    print("Experiment 3: ", time5)

    print("Deterministic quicksort experiments:")

    print("Experiment 1: ", time6)
    print("Experiment 2: ", time7)
    print("Experiment 3: ", time8)
