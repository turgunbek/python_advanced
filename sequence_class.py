from typing import Sequence, Any, Callable


class Seq:
    """
    Класс Sequence, который нужно реализовать. Содержит необходимые методы:

    __init__ - конструктор, принимающий любую последовательность Sequence[T],

    map - принимает функцию, которая будет трансформировать тип Т в любой тип,

    filter - принимает функцию, которая входным параметром принимает тип T
    и возвращает bool,

    take - принимает число и возвращает список из того количества элементов,
    которое передали в take.
    """

    def __init__(self, sequence: Sequence[Any]):
        self.sequence = sequence

    def map(self, func: Callable[[Any], Any]) -> "Seq":
        return map(func, self.sequence)

    def filter(self, func: Callable[[Any], bool]) -> "Seq":
        return filter(func, self.sequence)

    def take(self, number: int) -> "Seq":
        return Seq(self.sequence[:number])

    def __repr__(self):
        return repr(list(self.sequence))


if __name__ == '__main__':
    original_sequence = range(10)
    print(f'List of original sequence = {list(original_sequence)}')
    seq = Seq(original_sequence)

    mapped_seq = seq.map(lambda x: x ** 2)
    print(f'List of mapped Sequence = {list(mapped_seq)}')

    filtered_seq = seq.filter(lambda x: x % 2 == 0)
    print(f'List of filtered Sequence = {list(filtered_seq)}')

    take_4 = seq.take(4)
    print(f'Take 4 elements from original sequence: {take_4}')

    take_44 = seq.take(44)
    print(f'Take 44 (more than 10) elements from original sequence: {take_44}')

    lazy_map = seq.take(4).map(str)
    print(f'List of lazy map (by str) for 4 elements taken = {list(lazy_map)}')

    lazy_filter = seq.take(4).filter(lambda x: x % 2 == 0)
    print(f'List of lazy filter (of even numbers) for 4 elements taken ='
          f'{list(lazy_filter)}')

    # Out:
    # List of original sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List of mapped Sequence = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # List of filtered Sequence = [0, 2, 4, 6, 8]
    # Take 4 elements from original sequence: [0, 1, 2, 3]
    # Take 44 (more than 10) elements from original sequence:
    #       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List of lazy map (by str) for 4 elements taken = ['0', '1', '2', '3']
    # List of lazy filter (of even numbers) for 4 elements taken =[0, 2]
