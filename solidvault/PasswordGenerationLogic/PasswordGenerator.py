import random
import string


def generate_password(length: int, has_lowercase: bool, has_uppercase: bool, has_digits: bool,
                      has_special: bool) -> str:
    """
        Computes a password complying with the provided guidelines
    :param length: The length of the password
    :param has_lowercase: Whether the password can contain a lowercase letter (a, b, c, ...)
    :param has_uppercase: Whether the password can contain an uppercase letter (A, B, C, ...)
    :param has_digits: Whether the password can contain a digit (1, 2, 3, ...)
    :param has_special: Whether the password can contain a special character ($, %, /, ...)
    :return: The computer password
    """
    character_set = ""

    character_set += string.ascii_lowercase if has_lowercase else ""
    character_set += string.ascii_uppercase if has_uppercase else ""
    character_set += string.digits if has_digits else ""
    character_set += string.punctuation if has_special else ""

    return ''.join(random.choice(character_set) for _ in range(length)).replace(' ', '')
