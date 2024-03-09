
INT, OPERATOR, ADD, SUB = "int", "operator", '+', '-'


class Token:
    def __init__(self, key, value):
        self.type = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Operator(Token):
    def __init__(self):
        self.type = OPERATOR

    def operate(self, left, right):
        raise Exception("Not Implemented.")


class AddOperator(Operator):
    def __init__(self):
        self.value = ADD

    def operate(self, left, right):
        return left + right


class SubstractOperator(Operator):
    def __init__(self):
        self.value = SUB

    def operate(self, left, right):
        return left - right


class IntegerToken(Token):
    def __init__(self, value):
        self.key = int(value)


def operator_factory(op: Operator):
    if op == ADD:
        return AddOperator()
    elif op == SUB:
        return SubstractOperator()


def int_token_factory(value: int):
    return Token(
        INT,
        int(value)
    )


class Interpreter:
    def __init__(self, code: str):
        self.code = code
        self.curr = 0

        self.adder = AddOperator()
        self.subber = SubstractOperator()

        self.stack = []
        self.operator = None

    def process(self):
        for i in self.code:
            if self.operator:
                left = self.stack.pop()
                right = int_token_factory(i)
                return (
                    self.operator.operate(left.value, right.value)
                )
            if i.isdigit():
                if len(self.stack) > 0:
                    num = chr(i)
                    while len(self.stack) != 0:
                        num += str(self.stack.pop())
                    num = int(num[::-1])
                    current_token = int_token_factory(num)
                else:
                    current_token = int_token_factory(i)
                self.stack.append(current_token)
            else:
                self.operator = operator_factory(i)
        return self.stack.pop()

    def _get_stack(self):
        print(self.stack)


while True:
    code = input("code> ")
    i = Interpreter(code)
    print(i.process())
