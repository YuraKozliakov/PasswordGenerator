import re


class PasswordStrength:
    """
    Класс для проверки силы пароля.
    """

    @staticmethod
    def check_strength(password):
        """
        Проверяет силу пароля.
        """
        score = 0

        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'\d', password):
            score += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        return "Strong"
