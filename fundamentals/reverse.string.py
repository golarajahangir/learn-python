def solution(string):
    reversed_val = ""
    for n in reversed(range(0, len(string))):
        reversed_val = reversed_val + string[n]
    return reversed_val


# Best practice
def solution(str):
    return str[::-1]
