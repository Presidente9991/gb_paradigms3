"""
 Адаптер:
Создайте класс ElectricSocket, который имеет метод supply_electricity(voltage).
Реализуйте класс USPlugAdapter,
который адаптирует розетку стандарта США к европейскому стандарту.
Создайте объекты и продемонстрируйте передачу электроэнергии через адаптер.
"""


class ElectricSocket:
    @staticmethod
    def supply_electricity(voltage):
        print(f"Подача электричества напряжением {voltage} вольт")


class USPlugAdapter:
    def __init__(self, socket):
        self.socket = socket

    def supply_electricity(self, voltage):
        converted_voltage = voltage * 2.54
        self.socket.supply_electricity(converted_voltage)


euro_socket = ElectricSocket()
us_adapter = USPlugAdapter(euro_socket)
voltages = 110
us_adapter.supply_electricity(voltages)
