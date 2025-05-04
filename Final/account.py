from trees import BinarySearchTree


class Account:
    """
        Stores account number, title, and balance.
        Performs withdraw and deposit operations, and also
        is printable.
    """
    def __init__(self, number, title, balance=0.00):
        self.number = number
        self.title = title
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0.00:
            self.balance -= amount

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
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            target_acc.withdraw(amount)
        else:
            print("Account not found.")

    def delete_account(self, acc_num):
        """
            Takes in account number and locate it in the Binary Search Tree,
            delete the account if found.
        """
        
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
        
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            print(f"Balance: {target_acc.balance}")
        else:
            print("Account not found.")

    def traverse_preorder(self):
        """
            Traverses through the tree of accounts in pre-order,
            printing out each node visited
        """
        
        self.account_tree.traverse_preorder()

    def traverse_inorder(self):
        """
            Traverses through the tree of accounts in in-order,
            printing out each node visited
        """

        self.account_tree.traverse_inorder()

    def traverse_postorder(self):
        """
            Traverses through the tree of accounts in post-order,
            printing out each node visited
        """
        
        self.account_tree.traverse_postorder()

    
        