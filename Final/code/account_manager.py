# Komes Pispol ID: 90035701


from trees import BinarySearchTree
from account import Account


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

        new_acc = Account(number, str(title))
        self.account_tree.insert(number, new_acc)
        
        added_acc = self.account_tree.find(number)
        if added_acc is not None:
            print("Successfully created new account.")
            return True
        else:
            print("Error creating the account.")
            return False

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
            target_acc.withdraw(amount)
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
            return True
        else:
            print("Account not found.")
            return False

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
            return True
        else:
            print("Account not found.")
            return False

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
            return target_acc.balance
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

        return self.account_tree.traverse_inorder()

    def traverse_postorder(self):
        """
            Traverses through the tree of accounts in post-order,
            returns a queue of nodes in order.
        """
        
        return self.account_tree.traverse_postorder()


    
