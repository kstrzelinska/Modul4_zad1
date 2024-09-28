def is_palindrome(text):
    #ustawianie wszystkich małych liter i porównanie wyrazów czytanych od początku i od końca
    return text.lower() == text[::-1].lower()

print(is_palindrome("kajak"))
print(is_palindrome("Python"))