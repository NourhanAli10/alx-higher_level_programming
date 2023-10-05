#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if length == 4:
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, cal.add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, cal.sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, cal.mul(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, cal.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
