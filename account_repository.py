from account import Account


class MemoryAccountRepository:
    def __init__(self, accounts):
        self.accounts = accounts

    def find(self, account_id):
        return self.accounts[0]

    def save(self, account):
        return
