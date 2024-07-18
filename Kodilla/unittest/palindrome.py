def is_palindrome(word):
    word = word.lower().replace(' ', '')
    return word == word[::-1]

# Przykład użycia
print(is_palindrome("kajak"))  # Zwraca: True

def test_is_palindrome():
    assert is_palindrome("jablko") #fail
    assert is_palindrome("010010") #numbers
    assert is_palindrome("Kajak") #big/small letter
    assert is_palindrome("!_kajak_!") #symbols
test_is_palindrome()
