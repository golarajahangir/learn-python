def remove_every_other(my_list):
    keep_list = []

    for i, item in enumerate(my_list):
        if i % 2 == 0:
            keep_list.append(item)
    return keep_list


# best practice
def remove_every_other(my_list):
    return my_list[::2]
