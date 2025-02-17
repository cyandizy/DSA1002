#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    passes = 0
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - passes):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
        passes += 0


def insertionSort(A):
    for n in range(1, len(A)):
        i = n

    while (i > 0) and (A[i - 1] > A[i]):
        temp = A[i]
        A[i] = A[i - 1]
        A[i - 1] = temp

        i -= 1

def selectionSort(A):
    for n in range(0, len(A) - 1):
        min_idx = n
        for j in range(n + 1, len(A) - 1):
            if (A[j] < A[min_idx]):
                min_idx = j

        temp = A[min_idx]
        A[min_idx] = A[n]
        A[n] = temp

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


