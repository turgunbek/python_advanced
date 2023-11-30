import json
import keyword


class ColorizeMixin:
    repr_color_code = 0

    def __repr__(self):
        colored_text = (f'\033[{self.repr_color_code}'
                        f'm{super().__repr__()}\033[0m')
        return colored_text


class DictToObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, self._make_valid_attr_name(key), value)

    def _make_valid_attr_name(self, name):
        if keyword.iskeyword(name):
            return name + '_'
        return name


class Advert:
    def __init__(self, mapping):
        # Проверяем наличие обязательного атрибута title
        if 'title' not in mapping:
            print('Отсутствует обязательный атрибут "title" в JSON-объекте.')
        else:
            try:
                self.__dict__.update(DictToObject(mapping).__dict__)
            except AttributeError:
                pass

        # Присваиваем значения атрибутам динамически
        for key, value in mapping.items():
            setattr(self, key, value)

        # Проверяем и устанавливаем значение атрибута price
        self._price = 0
        if 'price' in mapping:
            self._price = mapping['price']

    def __getattr__(self, item):
        """Получение атрибута"""
        return self.__dict__.get(item, 0)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print('Цена должна быть положительной!')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def __str__(self):
        return self.__repr__()


class ColorizedAdvert(ColorizeMixin, Advert):
    repr_color_code = 33  # зеленый цвет


if __name__ == "__main__":
    print('-'*100)
    print('Пример 1: iPhone X | 100 ₽')
    iphone_ad_str = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    iphone = json.loads(iphone_ad_str)
    iphone_ad = Advert(iphone)
    print(iphone_ad)
    print(iphone_ad.location)

    print('-'*100)
    print('Пример 2: Отсутствие ключа "title"')
    lesson_str = """{
        "price": 1,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print('-'*100)
    print('Пример 3: отрицательный "price"')
    dog_str = """{
    "title": "Вельш-корги",
    "price": -1000,
    "class": "dogs"}"""

    dog = json.loads(dog_str)
    dog_ad = ColorizedAdvert(dog)
    print(dog_ad)
    print(dog_ad.class_)
    print(dog_ad.price)
