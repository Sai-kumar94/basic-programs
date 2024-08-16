# normal program


index_count=0
words='abcde'
for letter in words:
    print(words[index_count])
    index_count += 1


# using enumerate built-in function



words='abcde'
for item in enumerate(words):
    print(words)
    print(item)


# tuple unpacking


words='abcde'
for  index,letter in enumerate(words):
    print(index)
    print(letter)
    print()