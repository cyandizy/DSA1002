from dsa_heap import DSAHeapEntry


def heap_sort(arr):
    _heapify(arr, len(arr))
    for i in range((len(arr) - 1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _trickle_down(arr, i, 0)

def _heapify(arr, arr_len):
    for i in range((arr_len // 2) - 1, -1, -1):
        _trickle_down(arr, arr_len, i)


def _trickle_down(heap_arr, arr_len, current_idx):
    left_idx = (current_idx * 2) + 1
    right_idx = (current_idx * 2) + 2
    keep_going = True
    while keep_going and left_idx < arr_len:
        keep_going = False
        largest_idx = left_idx

        if right_idx < arr_len:
            if (heap_arr[left_idx] < 
                    heap_arr[right_idx]):
                largest_idx = right_idx

        if (heap_arr[largest_idx] > 
                heap_arr[current_idx]):
            temp = heap_arr[largest_idx]
            heap_arr[largest_idx] = heap_arr[current_idx]
            heap_arr[current_idx] = temp
            current_idx = largest_idx
            keep_going = True

        current_idx = largest_idx
        left_idx = (current_idx * 2) + 1
        right_idx = (current_idx * 2) + 2

if __name__ == "__main__":
    test = [DSAHeapEntry(i, None) for i in range(10, 0, -1)]
    for entry in test:
        print(entry.get_priority())
    heap_sort(test)
    print()
    for entry in test:
        print(entry.get_priority())
    
