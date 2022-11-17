# [1,2,3,9]   sum = 8
# [1,2,4,4]   sum = 8
# ordered


def google_sum(numbers_list, sum):
    result_list = []
    for number in numbers_list:
        second_number = sum - number
        if second_number in numbers_list:
            result_list.append((number, second_number))
    for item in result_list:
        if (item[1], item[0]) in result_list:
            result_list.remove((item[1], item[0]))
    return result_list


print(google_sum([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
