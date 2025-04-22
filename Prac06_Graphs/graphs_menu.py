# Edited from previous assignments

from graphs import DSAGraph

menu_dialogue = "Type \"help\" or \"h\" for the list of commands"
show_cmd = """\tList of commands:
                add_node {label}\t\tor\tan {label}
                add_edge {label1} {label2}\tor\tae {label} {label2}
                delete_node {label}\t\tor\tdn {label}
                delete_edge {label1} {label2}\tor\tde {label1} {label2}  
                display_list\t\t\tor\tdl
                display_matrix\t\t\tor\tdm
                breadth_first_search\t\tor\tbfs
                depth_first_search\t\tor\tdfs
                help\t\t\t\tor\th
                quit\t\t\t\tor\tq
"""
cmd = {
    "add_node": ["add_node", "an"],
    "add_edge": ["add_edge", "ae"],
    "delete_node" : ["delete_node", "dn"],
    "delete_edge": ["delete_edge", "de"],
    "display_list": ["display_list", "dl"],
    "display_matrix": ["display_matrix", "dm"],
    "breadth_first_search": ["breadth_first_search", "bfs"],
    "depth_first_search": ["depth_first_search", "dfs"],
    "help": ["help", "h"],
    "quit": ["quit", "q"],
}

prompt_dialogue = "Command> "

graph = DSAGraph()

print(menu_dialogue)
user_input = input(prompt_dialogue)
input_list = user_input.split(" ")
input_cmd = input_list[0]

while input_cmd not in cmd["quit"]:
    if input_cmd in cmd["add_node"]:
        if len(input_list) == 2:
            label = input_list[1]
            graph.add_vertex(label)
            if graph.has_vertex(label):
                print(f"Added node ({label}) to the graph.")
            else:
                print(f"Error adding node ({label}) to the graph.")

        elif len(input_list) < 2:
            print(f"Command [{input_cmd}] is missing an argument (label).")

        elif len(input_list) > 2:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["add_edge"]:
        if len(input_list) == 3:
            label1 = input_list[1]
            label2 = input_list[2]
            if not graph.has_vertex(label1) or not graph.has_vertex(label2):
                print(f"Node ({label1}) or ({label2}) is not in the graph.")
            else:
                if not graph.is_adjacent(label1, label2):
                    graph.add_edge(label1, label2)
                    if graph.is_adjacent(label1, label2):
                        print(f"Successfully linked ({label1}) to ({label2})")
                else:
                    print(f"Node ({label1}) and ({label2}) are already adjacent.")

        elif len(input_list) < 3:
            print(f"Command [{input_cmd}] is missing an argument or two.")

        elif len(input_list) > 3:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["delete_node"]:
        if len(input_list) == 2:
            label = input_list[1]
            graph.delete_node(label)

        elif len(input_list) < 2:
            print(f"Command [{input_cmd}] is missing an argument (label).")

        elif len(input_list) > 2:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["delete_edge"]:
        if len(input_list) == 3:
            label1 = input_list[1]
            label2 = input_list[2]
            if not graph.has_vertex(label1) or not graph.has_vertex(label2):
                print(f"Node ({label1}) or ({label2}) is not in the graph.")
            else:
                if graph.is_adjacent(label1, label2):
                    graph.delete_edge(label1, label2)
                    if not graph.is_adjacent(label1, label2):
                        print(f"Successfully remove edge connecting ({label1}) to ({label2})")
                else:
                    print(f"Node ({label1}) and ({label2}) are not adjacent.")

        elif len(input_list) < 3:
            print(f"Command [{input_cmd}] is missing an argument or two.")

        elif len(input_list) > 3:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["display_list"]:
        if len(input_list) == 1:
            graph.display_as_list()

        elif len(input_list) > 1:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["display_matrix"]:
        if len(input_list) == 1:
            graph.display_as_matrix()

        elif len(input_list) > 1:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["breadth_first_search"]:
        if len(input_list) == 1:
            graph.breadth_first_search()

        elif len(input_list) > 1:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["depth_first_search"]:
        if len(input_list) == 1:
            graph.depth_first_search()

        elif len(input_list) > 1:
            print(f"Command [{input_cmd}] has too many arguments.")

    elif input_cmd in cmd["help"]:
        print(show_cmd)

    elif input_cmd in cmd["quit"]:
        continue

    else:
        print(f"Unknown command: {input_cmd}")

    user_input = input(prompt_dialogue)
    input_list = user_input.split(" ")
    input_cmd = input_list[0]