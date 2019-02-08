from account import Account

class AccountService:
    def __init__(self, repository):
        self.repository = repository

    def update_balance(self, account_id, deposit):
        account = self.repository.find(account_id)
        account.add(deposit)
        self.repository.save(account)
        return account
