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

            lines.append(f"{d}{a:>{30 - len(d)}}")

        lines.append(f'Total: {self.balance}')

        return '\n'.join(lines)

    def deposit(self, amount, description=''):

        self.balance += amount
        self.ledger.append(
            {
                'amount': amount,
                'description': description
            }
        )

    def withdraw(self, amount, description=''):
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

    def get_withdraws_amount(self):

        withdraws = filter(lambda w: w['amount'] < 0, self.ledger)

        return sum(w['amount'] for w in withdraws)


def create_spend_chart(categories):

    # set total amount of withdraws
    total_amount = sum([c.get_withdraws_amount() for c in categories])

    # set arr with category data
    withdraws_percentage = [
        {'name': c.category_name,
         'amount': round(c.get_withdraws_amount() * 100 / total_amount),
         'sign': ' ' * 3}
        for c in categories
    ]

    bar_chart = 'Percentage spent by category\n'

    # get a bar chart
    for i in range(100, -1, -10):

        bar = ''

        for w in withdraws_percentage:
            if w['amount'] == i:
                w['sign'] = 'o  '
            bar += w['sign']

        bar_chart += str(i).rjust(3, ' ') + '| ' + bar + "\n"

        if i == 0:
            bar_chart += ' ' * 4 + '-' * (len(bar) + 1)


food = Category('Comida')
clothes = Category('Ropa')

food.deposit(1000, 'deposito inicial')
food.withdraw(10.15, 'golosina')
food.withdraw(15.89, 'restaurante y mas comida')

food.transfer(50, clothes)
food.transfer(1000, clothes)

clothes.deposit(1000)
clothes.withdraw(300)

print(create_spend_chart([food, clothes]))
