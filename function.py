class Expense:

    def __init__(self, name, category, amount, month, year) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.month = month
        self.year = year

    def __repr__(self) :
        return f"<Gasto: {self.name}, {self.category}, ${self.amount} >"
    

