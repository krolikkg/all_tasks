text = input("your words: ")
split_text = text.split()
split_text.sort(key = len)
print(" ".join(split_text))