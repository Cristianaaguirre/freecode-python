
class Category():

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.balance = 0

    def __str__(self) -> str:
        lines = [self.category_name.center(30, '*')]

        for item in self.ledger:
            d = item['description'][:23]
            a = '%.2f' % item['amount']

            lines.append( f"{d}{a:>{30-len(d)}}" )

        lines.append(f'Total: {self.balance}')

        return '\n'.join(lines)

    def deposit(self, amount, description = ''):

        self.balance += amount
        self.ledger.append(
            {
                'amount' : amount,
                'description' : description
            }
        )

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.deposit(-amount, description)

    def transfer(self, amount, budget_category):

        if self.check_funds(amount):

            self.withdraw(amount, f'Transfer to {budget_category.category_name}')
            budget_category.deposit(amount, f'Transfer from {self.category_name}')
            return True

        else:
            return False

    def check_funds(self, amount):
        return self.balance > amount


"""
- necestias los montos negativos
- necesitas calcular esos porcentajes

"""

def create_spen_chart(categories):

    arr = []

    for item in categories:

        name = item.category_name
        withdraws = filter(lambda x : x['amount'] < 0, item.ledger)

        amount = sum( [round(item['amount']) for item in withdraws] )

        arr.append((name, -amount))

    for i in range(100, -1, -10):
      formater = f""
      pass

    print(arr)


comida = Category('Comida')
ropa = Category('Ropa')

comida.deposit(1000, 'deposito inicial')
comida.withdraw(10.15, 'golosina')
comida.withdraw(15.89, 'restaurante y mas comida')

comida.transfer(50, ropa)
comida.transfer(1000, ropa)

# print(comida)

create_spen_chart([comida, ropa])


