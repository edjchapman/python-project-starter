class NotAStringError(ValueError):
    pass


def hello(name: str = "") -> str:
    if not isinstance(name, str):
        raise NotAStringError
    return f"Hello {name}"
