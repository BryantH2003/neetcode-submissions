class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digitStack = []
        opStack = []

        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators and len(digitStack) > 1:
                second = digitStack.pop()
                first = digitStack.pop()

                if token == "+":
                    digitStack.append(first + second)
                elif token == "-":
                    digitStack.append(first - second)
                elif token == "*":
                    digitStack.append(first * second)
                elif token == "/":
                    digitStack.append(int(first / second))
            else:
                digitStack.append(int(token))

        return int(digitStack[-1])
                