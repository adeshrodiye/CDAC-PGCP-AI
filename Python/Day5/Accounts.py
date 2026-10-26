class InvalidAmountError(Exception):
    pass
class ExceedsDepositLimitError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, acc_id, name, balance):
        self._acc_id = acc_id
        self._name = name
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    @property
    def name(self):
        return self._name

    @property
    def acc_id(self):
        return self._acc_id

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than 0!")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0!")
        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient funds in account!")
        self._balance -= amount
        return self._balance


class SavingAccount(Account):
    def __init__(self, acc_id, name, balance, acc_type="Personal"):
        super().__init__(acc_id, name, balance)
        self._acc_type = acc_type.lower()

    def deposit(self, amount: float) -> float:
        if amount > 100000:
            raise ExceedsDepositLimitError("Maximum up to 1 Lakh can be deposited at a time!")
        return super().deposit(amount)

    def withdraw(self, amount: float) -> float:
        min_balance = 0 if self._acc_type == "corporate" else 5000
        if self._balance - amount < min_balance:
            raise InsufficientBalanceError(f"Minimum balance of ₹{min_balance} must be maintained!")
        return super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def deposit(self, amount: float) -> float:
        if amount > 200000:
            raise ExceedsDepositLimitError("Maximum up to 2 Lakh can be deposited at a time!")
        return super().deposit(amount)

    def withdraw(self, amount: float) -> float:
        if self._balance - amount < 10000:
            raise InsufficientBalanceError("Minimum balance of ₹10,000 must be maintained!")
        return super().withdraw(amount)


