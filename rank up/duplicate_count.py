def duplicate_count(text):
    text = text.lower()
    counter = 0
    duplicate_char = []
    for item in text:
        if text.count(item) > 1 and item not in duplicate_char:
            counter += 1
            duplicate_char.append(item)

    return counter


print(duplicate_count("ABBA"))
