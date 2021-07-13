def int_func(word):
    return word.capitalize()

words = input("Ввведите слова чз пробел : ")
print(" ".join(map(int_func,words.split())))
