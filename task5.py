def is_palindrome(word):
    word = ''.join(char for char in word.lower() if char.isalnum())
    return word == word[::-1]


word1 = "racecar"
word2 = "hello"
print(is_palindrome(word1))
print(is_palindrome(word2))