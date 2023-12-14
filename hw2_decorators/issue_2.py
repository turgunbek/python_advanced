import sys
from datetime import datetime


def timed_output(function):
    original_write = sys.stdout.write

    def my_write(string_text):
        """Кастомная функция write для подмеы метода write у
        объекта sys.stdout. Допечатывая текущую метку времени
        """
        if string_text != "\n":
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            string_text = f"{timestamp}: {string_text}"
        original_write(string_text)

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


print_greeting("Avito")  # вывод с временной меткой
