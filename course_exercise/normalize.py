# TASK: improve name of variables DONE
# IMPROVE: let english numbers to stay instead of replace them from dictionary DONE
# R&D: use built-in methods instead of dictionary DONE
# IMPROVE: better and wiser solution DONE
# QUESTION: use input to get string from user DONE
# IMPROVE: test cases DONE


def normalize(string, parse_to_int=False):
    converted = ""
    numbers_table = {
        "۰": 0,
        "۱": 1,
        "۲": 2,
        "۳": 3,
        "۴": 4,
        "۵": 5,
        "۶": 6,
        "۷": 7,
        "۸": 8,
        "۹": 9,
    }
    for char in string:
        plus = str(numbers_table.get(char, char))
        # plus = str(numbers_table[char]) if char in numbers_table else char
        converted = converted + plus
    return int(converted) if parse_to_int else converted


# def normalize(str) -> str:
#     return str.translate(str.maketrans(dict(zip("۰۱۲۳۴۵۶۷۸۹", "0123456789"))))


print(type(normalize("12۳۴۵۹9", parse_to_int=True)))
