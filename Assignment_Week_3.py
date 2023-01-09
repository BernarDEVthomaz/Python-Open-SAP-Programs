letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
word = input("Please enter a sentence:")
word = word.lower()
newword = ""
for letter in word:
    if letter in letters:
        index = letters.index(letter)
        index = index + 5
        if index > 26:
            index = index % 26
        letter = letters[index]
    newword = newword + letter
print(newword)
