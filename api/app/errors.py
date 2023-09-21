class TagsException(Exception):
    pass


class TagsError(TagsException):
    error: str
    code: str

    def __init__(self, error: str, code: str):
        self.error = error
        self.code = code
        super().__init__()


class CannotSignInvalidIssuer(TagsException):
    pass
