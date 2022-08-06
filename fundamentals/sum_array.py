
# arr is None
# use min and max and sum methods
# use 1 for instead of 3!!
def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    max = arr[0]
    min = arr[0]
    for item in arr:
        if item < min:
            min = item
        if item > max:
            max = item
    arr.remove(min)
    arr.remove(max)
    sum = 0
    for item in arr:
        sum = sum + item
    return sum


# best practice
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0