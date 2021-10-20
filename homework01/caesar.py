import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    plaintext = list(map(ord, plaintext))
    for i in range(len(plaintext)):
        if 65 <= plaintext[i] <= 90:
            plaintext[i] += shift
            while plaintext[i] > 90:
                plaintext[i] -= 26
        elif 97 <= plaintext[i] <= 122:
            plaintext[i] += shift
            while plaintext[i] > 122:
                plaintext[i] -= 26
        plaintext[i] = chr(plaintext[i])
    line = ""
    ciphertext = line.join(plaintext)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    ciphertext = list(map(ord, ciphertext))
    for i in range(len(ciphertext)):
        if 65 <= ciphertext[i] <= 90:
            ciphertext[i] -= shift
            while ciphertext[i] < 65:
                ciphertext[i] += 26
        elif 97 <= ciphertext[i] <= 122:
            ciphertext[i] -= shift
            while ciphertext[i] < 97:
                ciphertext[i] += 26
        ciphertext[i] = chr(ciphertext[i])
    line = ""
    plaintext = line.join(ciphertext)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
