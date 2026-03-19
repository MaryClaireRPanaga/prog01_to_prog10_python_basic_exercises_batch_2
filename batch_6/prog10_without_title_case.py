# Program to convert each word to title case

s = input("Enter a string: ")

words = s.split()
title_words = []
for word in words:
    new_word = ""
    if len(word) > 0:
        # first character uppercase
        c = word[0]
        if 'a' <= c <= 'z':
            new_word += chr(ord(c) - 32)
        else:
            new_word += c

        # rest lowercase
        for c in word[1:]:
            if 'A' <= c <= 'Z':
                new_word += chr(ord(c) + 32)
            else:
                new_word += c

    title_words.append(new_word)

print(" ".join(title_words))