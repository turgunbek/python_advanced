import json
import keyword


class ColorizeMixin:
    """Миксин для текстового представления объектов класса Advert
    """
    def __init_subclass__(cls, **kwargs):
        """Установка отсутствующего значения поля repr_color_code
        для дочерних классов.
        """
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "repr_color_code"):
            cls.repr_color_code = 0

    def __repr__(self, text):
        """Для цветного вывода.
        """
        colored_text = f'\033[{self.repr_color_code}m{text}\033[0m'
        return colored_text


class Advert(ColorizeMixin):
    """Класс для динамического создания объектов из атрибутов JSON-объекта.
    Наследуется от миксина ColorizeMixin, который представляет текст в цвете.
    """
    repr_color_code = 33

    def __init__(self, mapping, root: bool = True):
        """Обработка входного словаря в формате JSON-объекта.
        """
        # Проверка наличия обязательного атрибута title
        try:
            if root and 'title' not in mapping:
                raise ValueError(
                    'Отсутствует обязательный атрибут "title" в JSON-объекте.'
                    )
        except ValueError as ve:
            print(f'ValueError: {ve}')

        self._price = 0  # Проверяем и устанавливаем значение атрибута price

        for key, value in mapping.items():
            if isinstance(value, dict):
                setattr(self, key, Advert(value, root=False))
            else:
                setattr(self, self._make_valid_attr_name(key), value)

    def _make_valid_attr_name(self, name):
        """Добавление '_' к имени атрибута, если он - ключевое слово
        """
        if keyword.iskeyword(name):
            return name + '_'
        return name

    def __getattr__(self, name):
        """Получение имени атрибута.
        """
        return self.__dict__.get(name, 0)

    def __setattr__(self, key, value):
        """Установка атрибута.
        """
        if key == 'price':
            try:
                if value < 0:
                    raise ValueError('Значение price должно быть >= 0.')
            except ValueError as ve:
                print(f'ValueError: {ve}')

        super().__setattr__(key, value)

    @property
    def price(self):
        """Представление поля price как атрибута объекта.
        """
        return self._price

    @price.setter
    def price(self, value):
        """Установка значения для атрибута price.
        """
        if value >= 0:
            self._price = value
        else:
            self._price = 0

    def __str__(self):
        """Строковое представление объекта.
        """
        return self.__repr__(f"{self.title} | {self.price} ₽")


if __name__ == "__main__":
    print('-'*100)
    print('Пример 1: красный Айфон')

    iphone_ad_str = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город N, улица Пушкина, дом Колотушкина",
            "metro_stations": ["Лужники", "Полянка"]
        }
    }"""

    iphone = json.loads(iphone_ad_str)
    iphone_ad = Advert(iphone)
    iphone_ad.repr_color_code = 31
    print(iphone_ad)  # Вывод красным цветом: iPhone X | 100 ₽
    print(iphone_ad.location.address)

    print('-'*100)
    print('Пример 2: жёлтый корги')

    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"}"""

    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    print(dog_ad)
    print(dog_ad.class_)
    print('Если установить значение price=-1, то:')
    dog_ad.price = -1
    print(f'Меняет на значение price={dog_ad.price}')

    print('-'*100)
    print('Пример 3: нет поля price')
    lesson_free_str = '{"title": "python"}'
    lesson_free = json.loads(lesson_free_str)
    lesson_free_ad = Advert(lesson_free)
    print(f'price = {lesson_free_ad.price}')

    print('-'*100)
    print('Пример 4: нет поля title')
    lesson_str = """{
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print('-'*100)
    print('End of program.')
