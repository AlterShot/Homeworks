class BankAccount:
    def __init__(self):
        self.__balance = 10

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("Баланс не может быть отрицательным")
        else:
            self.__balance = balance

    def check_balance(self):
        print(f"Текущий счет: {self.balance:.2f}")

    def add_to_balance(self):
        try:
            money_to_give = float(input("Сколько положить? "))
            self.balance += money_to_give
            print(f"{money_to_give} добавлено на счет")
        except ValueError:
            print("Некорректный ввод. Нужно число")

    def withdraw(self):
        try:
            money_to_take = float(input("Сколько снять? "))
            if money_to_take > self.balance:
                print("На счету столько нет")
            else:
                self.balance -= money_to_take
                print(f"{money_to_take} снято со счета")
        except ValueError:
            print("Некорректный ввод. Нужно число")
