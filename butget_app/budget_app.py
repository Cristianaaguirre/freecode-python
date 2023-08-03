# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-f-string


class Category():

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __str__(self) -> str:
        lines = [self.category_name.center(30, '*')]
        total = 0

        for i in self.ledger:
            d = i['description']
            a = i['amount']
            total += a

            lines.append(
                d[:23].ljust(23, ' ') + '{:.2f}'.format(a).rjust(7, ' ')
            )

        lines.append(f'Total: {total}')

        return '\n'.join(lines)

    def deposit(self, amount, description = ''):

        self.ledger.append(
            {
                'amount' : amount,
                'description' : description
            }
        )

    def withdraw(self, amount, description = ''):

        if not self.check_funds(amount):

            self.deposit(-amount, description)

    def get_balance(self):

        balance = 0

        for i in self.ledger:
            balance += i['amount']

        return balance


    def transfer(self, amount, budget_category):

        if not self.check_funds(amount):

            self.withdraw(amount, f'Transfer to {budget_category.category_name}')
            budget_category.deposit(amount, f'Transfer from {self.category_name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount > self.get_balance()

# def create_spen_chart(categories):
#     pass

comida = Category('Comida')
ropa = Category('Ropa')

comida.deposit(1000, 'deposito inicial')
comida.withdraw(10.15, 'golosina')
comida.withdraw(15.89, 'restaurante y mas comida')

comida.transfer(50, ropa)

print(comida)
