import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = quick_sort([x for x in arr[1:] if x <= pivot])
    right = quick_sort([x for x in arr[1:] if x > pivot])
    return left + [pivot] + right

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result