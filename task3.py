"""
Стратегия:
Реализуйте паттерн Стратегия на языке Python для сортировки списка чисел.
Создайте класс SortStrategy, имеющий метод sort(numbers), и несколько конкретных стратегий
для различных методов сортировки (например, пузырьковая сортировка, сортировка выбором).
"""


class SortStrategy:
    def sort(self, number):
        raise NotImplementedError("Подклассы должны реализовывать этот метод")

    @staticmethod
    def swap(number, i, j):
        number[i], number[j] = number[j], number[i]

    @staticmethod
    def print_info(number):
        print(number)


class BubbleSort(SortStrategy):
    def sort(self, number):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    self.swap(numbers, j, j + 1)
        print("Пузырьковая сортировка: ", end='')
        self.print_info(numbers)


class SelectionSort(SortStrategy):
    def sort(self, number):
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            self.swap(numbers, i, min_index)
        print('Сортировка выбором: ', end='')
        self.print_info(numbers)


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, number):
        self.strategy.sort(number)


if __name__ == '__main__':
    numbers = [33, 21, 55, 47, 13, 84, 61, 76, 1, 99]

    bobble_sort = BubbleSort()
    selection_sort = SelectionSort()

    context = Context(bobble_sort)
    context.sort(numbers)

    context.set_strategy(selection_sort)
    context.sort(numbers)
