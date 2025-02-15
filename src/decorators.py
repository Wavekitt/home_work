from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    декоратор, который создает логи
    """

    def logging_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)

                logs_message = f"{func.__name__} is ok, Result: {result}"

                if filename:
                    with open(filename, "a") as file:
                        file.write(logs_message + "\n")
                else:
                    print(logs_message)

                return result

            except Exception as error_:
                logs_message = f"{func.__name__} error: {error_}, input: {args}, {kwargs}"

                if filename:
                    with open(filename, "a") as file:
                        file.write(logs_message + "\n")
                else:
                    print(logs_message)

                raise

        return wrapper

    return logging_decorator
