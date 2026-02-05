# wrong_merge_sort.py

def merge_sort(arr):
    if len(arr) == 1:     # ❌ Problem 1: Doesn't handle empty array
        return arr

    mid = len(arr) // 2
    left = arr[:mid]     # ❌ Problem 2: Left half NOT sorted
    right = arr[mid:]   # ❌ Problem 3: Right half NOT sorted

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result        # ❌ Problem 4: Remaining elements ignored


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", arr)
    print("Sorted:", merge_sort(arr))



arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))
