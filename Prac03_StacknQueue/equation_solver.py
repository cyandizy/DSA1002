from stacks import Stack
from queues import CircularQueue


OPERATORS = ["+", "-", "*", "/"]

def solve(equation):
    equation = equation.replace(" ", "")
    postfix = _parse_infix_to_postfix(equation)
    result = _evaluate_postfix(postfix)
    for i in range(0, postfix.count()):
        print(postfix.dequeue(), end="")
    print(result)

def _parse_infix_to_postfix(equation):
    postfix = CircularQueue(len(equation))
    op_stacks = Stack(len(equation))
    num = ""
    for char in equation:
        if char.isdigit() or char == ".":
            num += char
        else:
            if num:
                postfix.enqueue(num)
                num = ""
            if char in OPERATORS:
                while not op_stacks.is_empty() and op_stacks.top() != "(" and _precedence_of(op_stacks.top()) >= _precedence_of(char):
                    popped = op_stacks.pop()
                    postfix.enqueue(popped)
                op_stacks.push(char)
            elif char == "(":
                op_stacks.push(char)
            elif char == ")":
                while not op_stacks.is_empty() and op_stacks.top() != "(":
                    popped = op_stacks.pop()
                    postfix.enqueue(popped)
                if op_stacks.is_empty():
                        raise ValueError("Parenthesis is not closed properly")
                op_stacks.pop()
            else:
                raise ValueError(f"Invalid value in equation: {char}")
    
    if num:
        postfix.enqueue(num)
        num = ""

    while not op_stacks.is_empty():
        popped = op_stacks.pop()
        postfix.enqueue(popped)

    return postfix


def _evaluate_postfix(postfix_queue):
    evaluation_stack = Stack(postfix_queue.count())
    while not postfix_queue.is_empty():
        if postfix_queue.peek() in OPERATORS:
            y = float(evaluation_stack.pop())
            x = float(evaluation_stack.pop())
            op = postfix_queue.dequeue()
            result = _execute_operation(op, x, y)
            evaluation_stack.push(result)
        else:
            evaluation_stack.push(postfix_queue.dequeue())
    return evaluation_stack.pop()

def _precedence_of(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2 
    else:
        raise ValueError(f"Unknown operator: {op}")

def _execute_operation(operator, x, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y

# print("Enter \"q\" to quit")
# prompt = "Equation> "
# user_input = input(prompt)

# while user_input != "q":
#     if user_input != "":
#         solve(user_input)
#     user_input = input(prompt)

postfix = CircularQueue(20)
postfix.enqueue("3")
postfix.enqueue("4")
postfix.enqueue("*")
postfix.enqueue("1")
postfix.enqueue("3")
postfix.enqueue("4")
postfix.enqueue("-")
postfix.enqueue("/")

print(_evaluate_postfix(postfix))
