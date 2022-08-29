# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
def in_array(array1, array2):
    r = []
    for arr1 in array1:
        for arr2 in array2:
            if arr1 in arr2:
                r.append(arr1)
    result = sorted(set(r))
    return list(result)


def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


print(
    in_array(
        ["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]
    )
)
