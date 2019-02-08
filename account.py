
class Account:
    def __init__(self, balance):
        self.balance = balance

    def add(self, deposit):
        self.balance = self.balance + deposit

