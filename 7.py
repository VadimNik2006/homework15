word = input("Введите слово: ")
new_word = []
for item in list(word[-1]):
    new_word.append(item)

print(new_word)