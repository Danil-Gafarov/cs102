def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    while len(keyword) < len(plaintext):
        keyword += keyword

    plaintext = list(map(ord, plaintext))
    keyword = list(map(ord, keyword))
    j = 0
    for i in range(len(plaintext)):
        if 65 <= plaintext[i] <= 90:
            plaintext[i] += (keyword[j] - 65)
            while plaintext[i] > 90:
                plaintext[i] -= 26
            j += 1
        elif 97 <= plaintext[i] <= 122:
            plaintext[i] += (keyword[j] - 97)
            while plaintext[i] > 122:
                plaintext[i] -= 26
            j += 1
        plaintext[i] = chr(plaintext[i])
    line = ""
    ciphertext = line.join(plaintext)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    while len(keyword) < len(ciphertext):
        keyword += keyword
    keyword = keyword.upper()
    ciphertext = list(map(ord, ciphertext))
    keyword = list(map(ord, keyword))
    j = 0
    for i in range(len(ciphertext)):
        if 65 <= ciphertext[i] <= 90:
            ciphertext[i] -= (keyword[j] - 65)
            while ciphertext[i] < 65:
                ciphertext[i] += 26
            j += 1
        elif 97 <= ciphertext[i] <= 122:
            ciphertext[i] -= (keyword[j] - 65)
            while ciphertext[i] < 97:
                ciphertext[i] += 26
            j += 1
        ciphertext[i] = chr(ciphertext[i])
    line = ""
    plaintext = line.join(ciphertext)
    return plaintext
