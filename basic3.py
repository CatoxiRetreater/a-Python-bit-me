def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    return word == reversed_word

input_word = "radar"
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")
