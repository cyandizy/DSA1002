from trees import BinarySearchTree

class Account:
    def __init__(self, number, title, balance=0):
        self.number = number
        self.title = title
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount


class AccountManager:
    def __init__(self):
        self.account_tree = BinarySearchTree()

    def new_account(self, number, title):
        new_acc = Account(number, title)
        self.account_tree.insert(number, new_acc)

    def deposit(self, acc_num, amount):
        target_acc: Account = self.account_tree.find(acc_num)
        target_acc.deposit(amount)

    def withdraw(self, acc_num, amount):
        target_acc: Account = self.account_tree.find(acc_num)
        target_acc.withdraw(amount)

    def delete_account(self, acc_num):
        self.account_tree.delete(acc_num)

    def search_account(self, acc_num):
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            print(f"""
                        Number: {target_acc.number}
                        Title: {target_acc.title}
                        Balance: {target_acc.balance}
                """)
        else:
            print("Account not found")

    def check_balance(self, acc_num):
        target_acc: Account = self.account_tree.find(acc_num)
        if target_acc is not None:
            print(f"Balance: {target_acc.balance}")
        else:
            print("Account not found.")

    def traverse_preorder(self):
        self.account_tree.traverse_preorder()

    def traverse_inorder(self):
        self.account_tree.traverse_inorder()

    def traverse_postorder(self):
        self.account_tree.traverse_postorder()

    
        