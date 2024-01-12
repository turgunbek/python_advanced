import sys
from datetime import datetime

# сохраним оригинальную функцию из sys.stdout
original_write = sys.stdout.write


def my_write(string_text):
    """Кастомная функция write для подмеы метода write у
    объекта sys.stdout. Допечатывая текущую метку времени
    """

    if string_text != "\n":
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        string_text = f"{timestamp}: {string_text}"
    original_write(string_text)


sys.stdout.write = my_write  # "подменяем" функцию

# вывод с временными метками
print('1, 2, 3')
print('Hello')
print(2 + 3)

# вернем сохраненную оригинальную функцию из sys.stdout
sys.stdout.write = original_write
print('Hello')  # вывод без временных меток
