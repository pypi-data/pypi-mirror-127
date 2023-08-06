from typing import Any, Dict


class ValidateException(Exception):
    """ The base class for all exception thrown by the validate decorator. """


class ValidationError(ValidateException):
    def __init__(self,
                 message: str = 'invalid parameter',
                 validator_name: str = '',
                 value: Any = None,
                 ) -> None:
        self.validator_name = validator_name
        self.value = value
        self.message = message

    def __str__(self) -> str:
        return f'Rule: {self.validator_name}, Value: {self.value}, Message: {self.message}'

    @property
    def to_dict(self) -> Dict[str, str]:
        return {
            'rule': self.validator_name,
            'value': str(self.value),
            'message': self.message,
        }


class InvalidHeader(ValidateException):
    """ Is raised if there is a validation error in a FlaskHeaderParameter. """


class TooManyArguments(ValidateException):
    """ Is raised if function got more arguments then expected. """
