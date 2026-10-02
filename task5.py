char = "A"

if len(char) == 1 and char.isalpha() and char.lower() in "aeiou":
    print("vowel")
else:
    print("not a vowel")