# def scramble(s1, s2):
#     for char in s2:
#         if char not in s1:
#             return False
#         if s1.count(char) < s2.count(char):
#             return False
#     return True

# def scramble(s1, s2):
#     list1 = list(s1)
#     list2 = list(s2)
#     for char in list1:
#         if char in list2:
#             list2.remove(char)
#         if len(list2) == 0:
#             return True
#     return False


# def scramble(s1, s2):
#     list1 = sorted(list(s1))
#     list2 = sorted(list(s2))
#     for char in list2:
#         if char not in list1:
#             return False
#         print(list1.index(char))
#         del list1[: list1.index(char)]
#         print(list2)
#         print(list1)

# return True


def scramble(s1, s2):
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))
    index_char = 0
    for char in list2:
        for i in range(index_char, len(list1)):
            if list1[i] == char:
                index_char = i + 1
                break
        else:
            return False
    return True


# best practice
def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


print(scramble("rkqodlw", "world"))
