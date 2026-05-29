def selection_sort(arr, descending=False):
    """Sort arr in-place using selection sort. Returns arr."""
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if descending:
                if arr[j] > arr[target_idx]:
                    target_idx = j
            else:
                if arr[j] < arr[target_idx]:
                    target_idx = j
        if target_idx != i:
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr
