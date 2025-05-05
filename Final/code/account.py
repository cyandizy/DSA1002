class Account:
    """
        Stores account number, title, and balance.
        Performs withdraw and deposit operations, and also
        is printable.
    """
    def __init__(self, number, title, balance=0.00):        
        self.title = title
        self.balance = float(balance)
        if not isinstance(number, int):
            raise TypeError("Account number must be number.")

        self.number = number

        if self.balance < 0.00:
            raise ValueError("Balance cannot be negative.")

    def deposit(self, amount):
        if isinstance(amount, str):
            raise TypeError("Amount must be numbers.") 
        
        if amount < 0.00:
            raise ValueError("Amount must be positive.")
        
        self.balance += amount

    def withdraw(self, amount):
        if isinstance(amount, str):
            raise TypeError("Amount must be numbers.") 
        
        if amount < 0.00:
            raise ValueError("Amount must be positive.")

        if self.balance - amount >= 0.00:
            self.balance -= amount
        else:
            raise ValueError("Not sufficient fund.")

    def __str__(self):
        return f"""
                        Number: {self.number}
                        Title: {self.title}
                        Balance: {self.balance}
                """
    

    def __repr__(self):
        self.__str__()


