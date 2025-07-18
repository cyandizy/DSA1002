# Improved from practical 6

from account_manager import AccountManager 
import readline # Allows command history


def validate_args(cmd_name, args): # Validates number of arguments required for a command
    current_cmd = cmd[cmd_name]
    expected_args = current_cmd["args"]
    
    if len(args) == len(expected_args):
        return True

    elif len(args) > len(expected_args):
        print(f"Command [{cmd_name}] has too many arguments.")

    elif len(args) < len(expected_args):
        print(f"Command [{cmd_name}] has too few arguments.")
    
    print(f"Correct format: {"/".join(current_cmd["aliases"])} {BOLD}{YELLOW}{" ".join(expected_args)}{RESET}")
    
    return False

menu_dialogue = "Type \"help\" or \"h\" for the list of commands"
prompt_dialogue = "Command> "


cmd = { # Stores aliases and arguments required for commands
    "add_account": {
        "aliases": ["add_account", "new_account", "add_acc", "new_acc", "add", "new"],
        "args": ["acc_num", "title"]
    },
    "delete_account": {
        "aliases": ["delete_account", "del_acc", "del"],
        "args": ["acc_num"]
    },
    "search_account": {
        "aliases": ["search_account", "search_acc", "search", "sa", "s"],
        "args": ["acc_num"]
    },
    "check_balance": {
        "aliases": ["check_balance", "check", "balance", "cb", "b"],
        "args": ["acc_num"]
    },
    "deposit": {
        "aliases": ["deposit", "d"],
        "args": ["acc_num", "amount"]
    },
    "withdraw": {
        "aliases": ["withdraw", "w"],
        "args": ["acc_num", "amount"]
    },
    "traverse_preorder": {
        "aliases": ["traverse_preorder", "preorder", "pre"],
        "args": []
    },
    "traverse_inorder": {
        "aliases": ["traverse_inorder", "inorder", "in"],
        "args": []
    },
    "traverse_postorder": {
        "aliases": ["traverse_postorder", "postorder", "post"],
        "args": []
    },
    "help": {
        "aliases": ["help", "h"],
        "args": []
    },
    "quit": {
        "aliases": ["quit", "q"],
        "args": []
    }
}

# Color escape characters
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

help_message = f"\t{BOLD}List of commands:{RESET}\n\n"
for name, attribute in cmd.items(): # Creates help text message from command dict 
    args_str = " ".join(f"{{{arg}}}" for arg in attribute["args"])
    aliases_str = "/".join(attribute['aliases'])
    help_message += f"\t{BOLD}{name} {args_str}{RESET}\n"
    help_message += f"\t\t{YELLOW} Aliases: {aliases_str} {RESET}\n"

# Initializes account manager for the session
account = AccountManager() 

print(menu_dialogue)
user_input = input(prompt_dialogue)
input_list = user_input.strip().split(" ")
input_cmd, *input_args = input_list

# Handles each command while the previous command is not "quit"
while input_cmd not in cmd["quit"]:
    if input_cmd in cmd["add_account"]["aliases"]:
        if validate_args("add_account", input_args):
            if input_args[0].isdigit():
                try:
                    account.new_account(int(input_args[0]), input_args[1])
                except Exception as e:
                    print(e)
            else:
                print("acc_num must be integer.")

    elif input_cmd in cmd["delete_account"]["aliases"]:
        if validate_args("delete_account", input_args):
            if input_args[0].isdigit():
                try:
                    account.delete_account(int(input_args[0]))
                except Exception as e:
                    print(e)
            else:
                print("acc_num must be integer.")

    elif input_cmd in cmd["search_account"]["aliases"]:
        if validate_args("search_account", input_args):
            if input_args[0].isdigit():
                try:
                    account.search_account(int(input_args[0]))
                except Exception as e:
                    print(e)
            else:
                print("acc_num must be integer.")

    elif input_cmd in cmd["check_balance"]["aliases"]:
        if validate_args("check_balance", input_args):
            if input_args[0].isdigit():
                try:
                    account.check_balance(int(input_args[0]))
                except Exception as e:
                    print(e)
            else:
                print("acc_num must be integer.")

    elif input_cmd in cmd["deposit"]["aliases"]:
        if validate_args("deposit", input_args):
            if input_args[0].isdigit() and input_args[1].isdigit():
                try:
                    account.deposit(int(input_args[0]), float(input_args[1]))
                except Exception as e:
                    print(e)
            else:
                print("acc_num and amount must be numbers.")

    elif input_cmd in cmd["withdraw"]["aliases"]:
        if validate_args("withdraw", input_args):
            if input_args[0].isdigit() and input_args[1].isdigit():
                try:
                    account.withdraw(int(input_args[0]), float(input_args[1]))
                except Exception as e:
                    print(e)
            else:
                print("acc_num and amount must be numbers.")

    elif input_cmd in cmd["traverse_preorder"]["aliases"]:
        if validate_args("traverse_preorder", input_args):
            traversal = account.traverse_preorder()
            while not traversal.is_empty():
                print(traversal.dequeue())

    elif input_cmd in cmd["traverse_inorder"]["aliases"]:
        if validate_args("traverse_inorder", input_args):
            traversal = account.traverse_inorder()
            while not traversal.is_empty():
                print(traversal.dequeue())
    
    elif input_cmd in cmd["traverse_postorder"]["aliases"]:
        if validate_args("traverse_postorder", input_args):
            traversal = account.traverse_postorder()
            while not traversal.is_empty():
                print(traversal.dequeue())

    elif input_cmd in cmd["help"]["aliases"]:
        print(help_message)

    elif input_cmd in cmd["quit"]["aliases"]:
        break

    else:
        print(f"Unknown command: {input_cmd}")

    user_input = input(prompt_dialogue)
    input_list = user_input.strip().split(" ")
    input_cmd, *input_args = input_list


