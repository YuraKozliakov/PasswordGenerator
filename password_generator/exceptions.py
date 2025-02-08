class InvalidInputError(Exception):
    """
    Исключение, которое выбрасывается, если введены некорректные данные.

    Attributes:
        message (str): Сообщение об ошибке.
    """

    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)
