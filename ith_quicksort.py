def quicksort(arr, i):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            if pivot_index == i:
                return arr[pivot_index]
            elif pivot_index < i:
                stack.append((pivot_index + 1, high))
            else:
                stack.append((low, pivot_index))

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right >= left:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

# Test data
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
i_value = 6
result = quicksort(my_list, i_value - 1)
print(f"The {i_value}th order statistic is: {result}")
