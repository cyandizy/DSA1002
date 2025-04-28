#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

import numpy as np


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
        minIdx = n
        for i in range(n + 1, len(A)):
            if (A[i] < A[minIdx]):
                minIdx = i

        temp = A[minIdx]
        A[minIdx] = A[n]
        A[n] = temp

def mergeSort(A):
    mergeSortRecurse(A, 0, len(A) - 1)

def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2

        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)

        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    tmpA = np.zeros(rightIdx - leftIdx + 1)
    i = leftIdx
    j = midIdx + 1
    k = 0

    while i <= midIdx and j <= rightIdx:
        if (A[i] <= A[j]):
            tmpA[k]= A[i]
            i += 1
        else:
            tmpA[k] = A[j]
            j += 1
        
        k += 1

    for i in range(i, midIdx + 1):
        tmpA[k] = A[i]
        k += 1
    
    for j in range(j, rightIdx + 1):
        tmpA[k] = A[j]
        k += 1

    for k in range(leftIdx, rightIdx + 1):
        A[k] = tmpA[k - leftIdx]


def quickSort(A):
    quickSortRecurse(A, 0, len(A) - 1)

def quickSortRecurse(A, leftIdx, rightIdx):
    if (rightIdx > leftIdx):
        piv_idx = (leftIdx + rightIdx) // 2
        new_piv_idx = doPartitioning(A, leftIdx, rightIdx, piv_idx)

        quickSortRecurse(A, leftIdx, new_piv_idx - 1)
        quickSortRecurse(A, new_piv_idx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pivValue = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivValue

    currentIdx = leftIdx

    for i in range(leftIdx, rightIdx):
        if (A[i] < pivValue):
            A[i], A[currentIdx] = A[currentIdx], A[i]
            
            currentIdx += 1

    newPivotIdx = currentIdx
    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivValue

    return newPivotIdx


