from trees import BinarySearchTree


class Account:
    """
        Stores account number, title, and balance.
        Performs withdraw and deposit operations, and also
        is printable.
    """
    def __init__(self, number, title, balance=0.00):        
        self.title = title
        self.balance = float(balance)

        if self.balance < 0.00:
            raise ValueError("Balance cannot be negative.")

    def deposit(self, amount):
        if isinstance(amount, str):
            raise TypeError("Amount must be numbers.") 
        
        self.balance += amount

    def withdraw(self, amount):
        if isinstance(amount, str):
            raise TypeError("Amount must be numbers.") 
        
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


class AccountManager:
    """
        Stores accounts using Binary Search Tree data structure.
        Performs account creation, deposit, withdraw, search,
        deletion, and traversals.
    """
    def __init__(self):
        self.account_tree = BinarySearchTree()

    def new_account(self, number, title):
        """
            Takes in account number and title, creates an Account object
            and append to the Binary Search Tree. 
        """
        if not isinstance(number, int):
            raise TypeError("Account number must be numbers.") 

        new_acc = Account(number, title)
        self.account_tree.insert(number, new_acc)
        
        added_acc = self.account_tree.find(number)
        if added_acc is not None:
            print("Successfully created new account.")
        else:
            print("Error creating the account.")

    def deposit(self, acc_num, amount):
        """
            Takes in account number and locate it in the Binary Search Tree,
            adds balance amount if found.
        """

        if not isinstance(acc_num, int):
            raise TypeError("Account number must be numbers.")
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount must be numbers.") 
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            target_acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, acc_num, amount):
        """
            Takes in account number and locate it in the Binary Search Tree,
            subtracts balance amount if found.
        """

        if not isinstance(acc_num, int):
            raise TypeError("Account number must be numbers.")
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount must be numbers.") 
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            try:
                target_acc.withdraw(amount)
            except ValueError as e:
                print(f"{e} Please try again.")
        else:
            print("Account not found.")

    def delete_account(self, acc_num):
        """
            Takes in account number and locate it in the Binary Search Tree,
            delete the account if found.
        """

        if not isinstance(acc_num, int):
            raise TypeError("Account number must be numbers.")
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            self.account_tree.delete(acc_num)
        else:
            print("Account not found.")

    def search_account(self, acc_num):
        """
            Takes in account number and locate it in the Binary Search Tree,
            prints out account details if found.
        """

        if not isinstance(acc_num, int):
            raise TypeError("Account number must be numbers.")
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            print(f"""
                        Number: {target_acc.number}
                        Title: {target_acc.title}
                        Balance: {target_acc.balance}
                """)
        else:
            print("Account not found.")

    def check_balance(self, acc_num):
        """
            Takes in account number and locate it in the Binary Search Tree,
            prints out account balance if found.
        """

        if not isinstance(acc_num, int):
            raise TypeError("Account number must be numbers.")
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            print(f"Balance: {target_acc.balance}")
        else:
            print("Account not found.")

    def traverse_preorder(self):
        """
            Traverses through the tree of accounts in pre-order,
            returns a queue of nodes in order.
        """

        return self.account_tree.traverse_preorder()

    def traverse_inorder(self):
        """
            Traverses through the tree of accounts in in-order,
            returns a queue of nodes in order.
        """

        return self.account_tree.traverse_preorder()

    def traverse_postorder(self):
        """
            Traverses through the tree of accounts in post-order,
            returns a queue of nodes in order.
        """
        
        return self.account_tree.traverse_preorder()

    
        