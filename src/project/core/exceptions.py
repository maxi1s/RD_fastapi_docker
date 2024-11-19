from typing import Final


class UserNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "User с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class UserAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Пользователь с почтой '{email}' уже существует"

    def __init__(self, email: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(email=email)
        super().__init__(self.message)

class FlowerAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Такой цветок уже есть"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)

class FlowerNotFound(BaseException):
    "Исключение, вызываемое, когда цветок не найден."
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Цветок с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class FlowerNotFound(Exception):
    def __init__(self, message="Цветок не найден"):
        self.message = message
        super().__init__(self.message)
