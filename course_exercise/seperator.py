# def seperator(number):
#     new = list(number[::-1])
#     list2 = []
#     for i in range(0, len(new), 3):
#         i = i + 3
#         new.insert(i, ",")
#     result = "".join(new[::-1])
#     print("rr", result)

#     print("result", result)
#     return
def seperator(number):
    list1 = list(number[::-1])
    list2 = []
    for index, value in enumerate(list1):
        x = index + 1
        list2.append(value)
        if x % 3 == 0 and x != len(list1):
            list2.append(",")

    result = "".join(list2[::-1])
    return result


# def seperator(number):
#     list1 = list(number)
#     list2 = []
#     for index in range(len(list1) - 1, -1, -1):
#         x = index + 1
#         list2.append(list1[index])
#         if x % 3 == 0:
#             list2.append(",")
#     result = "".join(list2[::-1])
#     print(result)
#     return result


seperator("122234567890")
