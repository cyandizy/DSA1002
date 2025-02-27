#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    swapped = False
    for i in range(0, len(A)):
        for j in range(1, len(A) - i):
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp

                swapped = True

        if not swapped:
            break


def insertionSort(A):
    for n in range(1, len(A)):
        i = n

        while i > 0 and A[i - 1] > A[i]:
            temp = A[i]
            A[i] = A[i - 1]
            A[i - 1] = temp

            i -= 1

def selectionSort(A):
    for n in range(0, len(A)):
        min_idx = n
        for i in range(n + 1, len(A)):
            if (A[i] < A[min_idx]):
                min_idx = i

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


