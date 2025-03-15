from dsa_linked_list import DSALinkedList

menu_dialogue = "Type \"help\" or \"h\" for the list of commands"
show_commands = """\tList of commands:
                insert_first {value}\tor\tif {value}
                insert_last {value}\tor\til {value}
                remove_first\t\tor\trf
                remove_last\t\tor\trl
                peek_first\t\tor\tpf
                peek_last\t\tor\tpl
                display\t\t\tor\td
                help\t\t\tor\th
                quit\t\t\tor\tq
"""
commands = {
    "insert_first": ["insert_first", "if"],
    "insert_last" : ["insert_last", "il"],
    "remove_first": ["remove_first", "rf"],
    "remove_last": ["remove_last", "rl"],
    "peek_first": ["peek_first", "pf"],
    "peek_last": ["peek_last", "pl"],
    "display": ["display", "d"],
    "help": ["help", "h"],
    "quit": ["quit", "q"],
}

prompt_dialogue = "Command> "

linked_list = DSALinkedList()

print(menu_dialogue)
user_input = input(prompt_dialogue)
input_command = user_input.split(" ")

while input_command[0] != "quit":
    if input_command[0] in commands["insert_first"]:
        if len(input_command) == 2:
            linked_list.insert_first(input_command[1])
            print(f"Inserted ({input_command[1]}) at the front")
        
        elif len(input_command) < 2:
            print(f"Command [{input_command[0]}] is missing an argument (value).")

        elif len(input_command) > 2:
            print(f"Command [{input_command[0]}] has too many arguments.")


    elif input_command[0] in commands["insert_last"]:
        if len(input_command) == 2:
            linked_list.insert_last(input_command[1])
            print(f"Inserted ({input_command[1]}) at the back")
        
        elif len(input_command) < 2:
            print(f"Command [{input_command[0]}] is missing an argument (value).")

        elif len(input_command) > 2:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["remove_first"]:
        if len(input_command) == 1:
            if not linked_list.is_empty():
                removed = linked_list.remove_first()
                print(f"First element ({removed}) has been removed.")
            else:
                print("Linked list is empty")
    
        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["remove_last"]:
        if len(input_command) == 1:
            if not linked_list.is_empty():
                removed = linked_list.remove_last()
                print(f"Last element ({removed}) has been removed.")
            else:
                print("Linked list is empty")

        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["peek_first"]:
        if len(input_command) == 1:
            peeked = linked_list.peek_first()
            print(f"The first element is {peeked}.")

        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["peek_last"]:
        if len(input_command) == 1:
            peeked = linked_list.peek_last()
            print(f"The last element is {peeked}.")

        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")


    elif input_command[0] in commands["display"]:
        if len(input_command) == 1:
            print(linked_list.display())

        elif len(input_command) > 1:
            print(f"Command [{input_command[0]}] has too many arguments.")

    elif input_command[0] in commands["help"]:
        print(show_commands)

    elif input_command[0] in commands["quit"]:
        break

    else:
        print(f"Unknown command: {input_command[0]}")

    user_input = input(prompt_dialogue)
    input_command = user_input.split(" ")


