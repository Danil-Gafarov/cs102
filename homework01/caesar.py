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
    plaintext_list = list(map(ord, plaintext))
    for i in range(len(plaintext_list)):
        if 65 <= plaintext_list[i] <= 90:
            plaintext_list[i] += shift
            while plaintext_list[i] > 90:
                plaintext_list[i] -= 26
        elif 97 <= plaintext_list[i] <= 122:
            plaintext_list[i] += shift
            while plaintext_list[i] > 122:
                plaintext_list[i] -= 26
    line = ""
    ciphertext = line.join(map(chr, plaintext_list))
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
    ciphertext_list = list(map(ord, ciphertext))
    for i in range(len(ciphertext_list)):
        if 65 <= ciphertext_list[i] <= 90:
            ciphertext_list[i] -= shift
            while ciphertext_list[i] < 65:
                ciphertext_list[i] += 26
        elif 97 <= ciphertext_list[i] <= 122:
            ciphertext_list[i] -= shift
            while ciphertext_list[i] < 97:
                ciphertext_list[i] += 26
    line = ""
    plaintext = line.join(map(chr, ciphertext_list))
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
