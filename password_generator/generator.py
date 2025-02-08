import random
import string
from password_generator.exceptions import InvalidInputError


class PasswordGenerator:
    """
    Класс для генерации паролей на основе заданных критериев.
    """

    def __init__(self, length, use_digits, use_special_chars, use_uppercase):
        self.length = length
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars
        self.use_uppercase = use_uppercase

    def generate(self):
        """
        Генерирует пароль на основе настроек.
        """
        if self.length < 6:
            raise InvalidInputError("Password length must be at least 6 characters.")

        characters = string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        if self.use_uppercase:
            characters += string.ascii_uppercase

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
