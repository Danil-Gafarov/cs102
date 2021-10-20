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
    keyword = keyword.upper()
    plaintext_list = list(map(ord, plaintext))
    keyword_list = list(map(ord, keyword))
    j = 0
    for i in range(len(plaintext_list)):
        if 65 <= plaintext_list[i] <= 90:
            plaintext_list[i] += keyword_list[j] - 65
            while plaintext_list[i] > 90:
                plaintext_list[i] -= 26

        elif 97 <= plaintext_list[i] <= 122:
            plaintext_list[i] += keyword_list[j] - 65
            while plaintext_list[i] > 122:
                plaintext_list[i] -= 26
        j += 1
    line = ""
    ciphertext = line.join(map(chr, plaintext_list))
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
    ciphertext_list = list(map(ord, ciphertext))
    keyword_list = list(map(ord, keyword))
    '''
    plaintext_list = list(map(ord, plaintext))
    keyword_list = list(map(ord, keyword))
    '''

    j = 0
    for i in range(len(ciphertext_list)):
        if 65 <= ciphertext_list[i] <= 90:
            ciphertext_list[i] -= keyword_list[j] - 65
            while ciphertext_list[i] < 65:
                ciphertext_list[i] += 26

        elif 97 <= ciphertext_list[i] <= 122:
            ciphertext_list[i] -= keyword_list[j] - 65
            while ciphertext_list[i] < 97:
                ciphertext_list[i] += 26
        j += 1
    line = ""
    plaintext = line.join(map(chr, ciphertext_list))
    return plaintext
