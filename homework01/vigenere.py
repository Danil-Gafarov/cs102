def encrypt_vigenere(plaintext: str, keyword: str) -> str:

    while len(keyword) < len(plaintext):
        keyword += keyword
    keyword = keyword.upper()

    ciphertext = ""
    j = 0  # счётчик для перебора ключа
    for char in plaintext:
        shift = ord(keyword[j]) - ord("A")
        if char.isupper():
            ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char
        j += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    while len(keyword) < len(ciphertext):
        keyword += keyword
    keyword = keyword.upper()

    plaintext = ""
    j = 0
    for char in ciphertext:
        shift = ord(keyword[j]) - ord("A")
        if char.isupper():
            plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        elif char.islower():
            plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))

        else:
            plaintext += char
        j += 1
    return plaintext
