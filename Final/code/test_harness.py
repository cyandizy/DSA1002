import unittest
from account import Account
from account_manager import AccountManager

class TestAccount(unittest.TestCase):
    """
        Test cases for all methods of Account Class
    """
    def test_constructor(self):
        number = [1, 2, "C"]
        title = ["A", "B", "C"]
        balance = [1000, -1000, 1000]

        expected = [(1, "A", "1000.00"), ValueError, TypeError]

        msg = ["Intended Case", "Negative balance", "Non-digits account number"]
        
        for i in range(len(number)):
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    Account(number[i], title[i], balance[i])
            elif expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    Account(number[i], title[i], balance[i])
            else:
                account = Account(number[i], title[i], balance[i])
                self.assertEqual(expected[i], (account.number, account.title, f"{account.balance:.2f}"))
        

    def test_deposit(self):
        amount = [1000, -1000, "A"]
        expected = [1000, ValueError, TypeError]
        msg = ["Intended Case", "Negative amount", "Non-digits amount"]
        for i in range(len(amount)):
            account = Account(1, "Test")
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    account.deposit(amount[i])
            elif expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    account.deposit(amount[i])
            else:
                account.deposit(amount[i])
                self.assertEqual(expected[i], account.balance)


    def test_withdraw(self):
        amount = [1000, -1000, "A", 99999]
        expected = [9000.0, ValueError, TypeError, ValueError]
        msg = ["Intended Case", "Negative amount", "Non-digits amount", "Not sufficient fund"]
        for i in range(len(amount)):
            account = Account(1, "Test", 10000.00)
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    account.withdraw(amount[i])
            elif expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    account.withdraw(amount[i])
            else:
                account.withdraw(amount[i])
                self.assertEqual(expected[i], account.balance)

class TestAccountManager(unittest.TestCase):
    """
        Test cases for all methods of AccountManager Class
    """
    def test_new_account(self):
        number = [1, "C"]
        title = ["A", "C"]
        expected = [True, TypeError]
        msg = ["Intended Case", "Non-digit account number"]

        for i in range(len(number)):
            test = AccountManager()
            if expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.new_account(number[i], title[i])
            else:                
                self.assertEqual(expected[i], test.new_account(number[i], title[i]), msg[i])

    def test_deposit(self):
        amount = [1000, -1000, "A"]
        expected = [1000, ValueError, TypeError]
        msg = ["Intended Case", "Negative amount", "Non-digits amount"]
        for i in range(len(amount)):
            test = AccountManager()
            test.new_account(1, "test")
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    test.deposit(1, amount[i])
            elif expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.deposit(1, amount[i])
            else:
                test.deposit(1, amount[i])
                self.assertEqual(expected[i], test.check_balance(1))

    def test_withdraw(self):
        amount = [1000, -1000, "A", 99999]
        expected = [9000.0, ValueError, TypeError, ValueError]
        msg = ["Intended Case", "Negative amount", "Non-digits amount", "Not sufficient fund"]
        for i in range(len(amount)):
            test = AccountManager()
            test.new_account(1, "test")
            test.deposit(1, 10000)
            if expected[i] is ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    test.withdraw(1, amount[i])
            elif expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.withdraw(1, amount[i])
            else:
                test.withdraw(1, amount[i])
                self.assertEqual(expected[i], test.check_balance(1))


    def test_delete_account(self):
        number = [1, "C", 2]
        expected = [True, TypeError, False]
        msg = ["Intended Case", "Non-digit account number", "Account not found"]

        for i in range(len(number)):
            test = AccountManager()
            test.new_account(1, "test")
            if expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.delete_account(number[i])
            else:                
                self.assertEqual(expected[i], test.delete_account(number[i]), msg[i])

    def test_search_account(self):
        number = [1, "C", 2]
        expected = [True, TypeError, False]
        msg = ["Intended Case", "Non-digit account number", "Account not found"]

        for i in range(len(number)):
            test = AccountManager()
            test.new_account(1, "test")
            if expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.search_account(number[i])
            else:                
                self.assertEqual(expected[i], test.search_account(number[i]), msg[i])

    def test_check_balance(self):
        number = [1, "C", 2]
        expected = [0.0, TypeError, None]
        msg = ["Intended Case", "Non-digit account number", "Account not found"]

        for i in range(len(number)):
            test = AccountManager()
            test.new_account(1, "test")
            if expected[i] is TypeError:
                with self.assertRaises(TypeError, msg=msg[i]):
                    test.check_balance(number[i])
            else:                
                self.assertEqual(expected[i], test.check_balance(number[i]), msg[i])


    def test_traverse_preorder(self):
        test = AccountManager()
        test.new_account(2, "B")
        test.new_account(1, "A")
        test.new_account(3, "C")
        traversal = test.traverse_preorder()
        expected = [2, 1, 3]
        actual = []
        msg = "Traversal not in correct order"
        while not traversal.is_empty():
            actual.append(traversal.dequeue().number)
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i], msg)

    def test_traverse_inorder(self):
        test = AccountManager()
        test.new_account(2, "B")
        test.new_account(1, "A")
        test.new_account(3, "C")
        traversal = test.traverse_inorder()
        expected = [1, 2, 3]
        actual = []
        msg = "Traversal not in correct order"
        while not traversal.is_empty():
            actual.append(traversal.dequeue().number)
        
        print(actual)

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i], msg)

    def test_traverse_postorder(self):
        test = AccountManager()
        test.new_account(2, "B")
        test.new_account(1, "A")
        test.new_account(3, "C")
        traversal = test.traverse_postorder()
        expected = [1, 3, 2]
        actual = []
        msg = "Traversal not in correct order"
        while not traversal.is_empty():
            actual.append(traversal.dequeue().number)
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i], msg)