from abc import abstractmethod, ABC


class PokemonTrainInterface(ABC):
    """
    Абстрактный класс тренировок покемонов, который содержит методы:
    increase_experience,
    experience
    """

    @abstractmethod
    def increase_experience(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def experience(self) -> int:
        pass


class BasePokemon(PokemonTrainInterface):
    """
    Базовый класс для покемонов, который содержит поля:
    name - имя покемона,
    poketype - тип покемона,
    _experience - количество опыта, по умолчанию равно 100
    Переопределяет метод строкового представления объекта __str__
    Наследуется от абстрактного класса PokemonTrainInterface, есть методы:
    increase_experience - увеличить опыт
    experience - установить значение опыта
    """

    def __init__(self, name: str, poketype: str):
        """
        конструктор, инициализирующий имя и тип покемона, а также
        начальный опыт
        """
        self.name = name
        self.poketype = poketype
        self._experience = 100

    def __str__(self) -> str:
        """магический метод для определения строкового представления объекта
        """
        return f'{self.name}/{self.poketype}'

    def increase_experience(self, value: int) -> None:
        """увеличивает опыт на величину value
        """
        self.experience += value

    @property
    def experience(self) -> int:
        """выводит значение опыта покемона
        """
        return self._experience

    @experience.setter
    def experience(self, value) -> int:
        """устанавливает в поле _experience заданное значение value
        """
        self._experience = value


class EmojiMixIn:
    """
    Миксин, который модифицирует метод __str__ заменой категории на эмоджи
    """

    emojis = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡'}

    def __str__(self):
        return f'{self.name}/{self.emojis[self.poketype]}'


class Pokemon(EmojiMixIn, BasePokemon):
    """
    Класс для покемонов Pokemon, который наследуется от родительских классов
    EmojiMixIn и BasePokemon
    """
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(f'pokemon = {bulbasaur}, experience = {bulbasaur.experience}')
    # Out:
    # pokemon = Bulbasaur/🌿, pokemon's experience = 100

    bulbasaur.increase_experience(100)
    print('After increasing exp:')
    print(f'pokemon = {bulbasaur}, experience = {bulbasaur.experience}')
    # Out:
    # After increasing exp:
    # pokemon = Bulbasaur/🌿, pokemon's experience = 200

    assert bulbasaur.experience == 200, 'Try harder, Neeman'

    pikachu = Pokemon(name='Pikachu', poketype='electric')
    print(pikachu)
    # Out:
    # Pikachu/⚡

    pikachu.increase_experience(42)
    print('After increasing exp:')
    print(f'pokemon = {pikachu}, experience = {pikachu.experience}')
    # Out:
    # After increasing exp:
    # pokemon = Pikachu/⚡, experience = 142
