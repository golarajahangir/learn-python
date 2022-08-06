def reverse_seq(n):
    reverse_list = []
    for i in range(0, n):
        reverse_list.append(n - i)

    return reverse_list


# best practice
def reverseseq(n):
    return range(n, 0, -1)
