import unittest
from account import *

class TestAccount(unittest.TestCase):
    def test_constructor(self):
        number = [1, 2, "C"]
        title = ["A", "B", "C"]
        balance = [1000, -1000, 1000]
        msg = ["Intended Case", "Negative balance", "Non-digits account number"]

        expected = [(1, "A", "1000.00"), ValueError, ValueError]

        for i in range(len(number)):
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    Account(number[i], title[i], balance[i])
            else:
                account = Account(number[i], title[i], balance[i])
                self.assertEqual(expected[i], (account.number, account.title, f"{account.balance:.2f}"))
        

    def test_deposit(self):
        amount = [1000, ]

    def test_withdraw():
        ...

class TestAccountManager(unittest.TestCase):
    def test_new_account():
        ...

    def test_deposit():
        ...

    def test_withdraw():
        ...

    def test_delete_account():
        ...

    def test_search_account():
        ...

    def test_check_balance():
        ...

    def test_traverse_preorder():
        ...

    def test_traverse_inorder():
        ...

    def test_traverse_postorder():
        ...