from trees import BinarySearchTree

menu_dialogue = "Type \"help\" or \"h\" for the list of commands"
show_commands = """\tList of commands:
                add {key} {value}\tor\ta {key} {value}
                find {key}\t\tor\tf {key} 
                delete {key}\t\tor\tdel {key} 
                display\t\t\tor\td
                height\t\t\tor\tht
                balance\t\t\tor\tb
                min\t\t\tor\tmn
                max\t\t\tor\tmx
                help\t\t\tor\th
                quit\t\t\tor\tq
"""
commands = {
    "add": ["add", "a"],
    "find": ["find", "f"],
    "delete" : ["delete", "del"],
    "display": ["display", "d"],
    "height": ["height", "ht"],
    "balance": ["balance", "b"],
    "min": ["min", "mn"],
    "max": ["max", "mx"],
    "help": ["help", "h"],
    "quit": ["quit", "q"],
}

prompt_dialogue = "Command> "
display_prompt = "Preorder, inorder, or postorder?> "

tree = BinarySearchTree()

print(menu_dialogue)
user_input = input(prompt_dialogue)
input_command = user_input.split(" ")

while input_command[0] != "quit":
    if input_command[0] in commands["add"]:
        if len(input_command) == 2:
            tree.insert(input_command[1])
            print(f"Inserted ({input_command[1]}) to the binary tree.")

        elif len(input_command) == 3:
            tree.insert(input_command[1], input_command[2])
            print(f"Inserted {input_command[2]}({input_command[1]}) to the binary tree.")
        
        elif len(input_command) < 2:
            print(f"Command [{input_command[0]}] is missing an argument (key).")

        elif len(input_command) > 3:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["find"]:
        if len(input_command) == 2:
            value = tree.find(input_command[1])
            if value != None:
                print(value)
            else:
                print(f"No key ({input_command[1]}) in the tree.")
        
        elif len(input_command) < 2:
            print(f"Command [{input_command[0]}] is missing an argument (key).")

        elif len(input_command) > 2:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["delete"]:
        if len(input_command) == 2:
            if tree.find(input_command[1]) != None:
                tree.delete(input_command[1])
                print(f"Removed ({input_command[1]}) from the binary tree.")
            else:
                print(f"Key ({input_command[1]}) is not in the binary tree.")
        
        elif len(input_command) < 2:
            print(f"Command [{input_command[0]}] is missing an argument (key).")

        elif len(input_command) > 2:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["display"]:
        if len(input_command) == 1:
            display_mode = input(display_prompt).lower();
            if display_mode == "preorder":
                tree.transverse_preorder()
            elif display_mode == "inorder":
                tree.transverse_inorder()
            elif display_mode == "postorder":
                tree.transverse_postorder()

        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["height"]:
        print(f"The tree has {tree.height()} levels (including root).")

    elif input_command[0] in commands["balance"]:
        print(f"The tree is {tree.balance()} balance.")
        
    elif input_command[0] in commands["min"]:
        key, value = tree.min()
        print(f"The minimum key is {value}({key}).")
        
    elif input_command[0] in commands["max"]:
        key, value = tree.max()
        print(f"The maximum key is {value}({key}).")

    elif input_command[0] in commands["help"]:
        print(show_commands)

    elif input_command[0] in commands["quit"]:
        break

    else:
        print(f"Unknown command: {input_command[0]}")

    user_input = input(prompt_dialogue)
    input_command = user_input.split(" ")


