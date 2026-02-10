


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    

    return result


arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))
