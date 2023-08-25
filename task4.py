"""
Декоратор:
Создайте класс Coffee с методом cost(), возвращающим стоимость кофе.
Реализуйте декораторы Sugar и Milk, которые добавляют сахар и молоко к кофе, соответственно.
Создайте объект кофе и последовательно примените к нему декораторы, затем выведите общую стоимость
"""


class Coffee:
    @staticmethod
    def cost():
        return 25


class Sugar:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 4


class Milk:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 8


simple_coffee = Coffee()
coffee_with_sugar = Sugar(simple_coffee)
coffee_with_milk = Milk(simple_coffee)
two_in_one_coffee = Milk(coffee_with_sugar)

print(f"Стоимость кофе: {simple_coffee.cost()}")
print(f"Стоимость кофе с сахаром: {coffee_with_sugar.cost()}")
print(f"Стоимость кофе с молоком: {coffee_with_milk.cost()}")
print(f"Стоимость кофе с сахаром и молоком: {two_in_one_coffee.cost()}")
