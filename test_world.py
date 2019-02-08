from account import Account
from account_service import AccountService
from account_repository import MemoryAccountRepository

def test_update_balance():
    accounts = [Account(100), Account(200)]
    r = MemoryAccountRepository(accounts)
    service = AccountService(r)

    account = service.update_balance(12323, 25)
    assert account.balance == 125