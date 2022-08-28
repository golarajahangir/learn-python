sentence = "This is a common interview question"
count_char = {}
for char in sentence:
    count_char[char] = sentence.count(char)

max_value = max(count_char, key=count_char.get)
print(max_value)
