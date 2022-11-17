def count_by(x, n):
    list = []
    for times in range(1, n + 1):
        list.append(x * times)

    return list


print(count_by(2, 5))
