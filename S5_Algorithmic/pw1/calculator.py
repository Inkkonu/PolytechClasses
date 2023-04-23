import re


def calculator() -> int:
    print("Type an operation (must end with an equal)")
    s = input()
    if re.match("[ ]*[0-9]{1,}[ ]*([+\-*%]{1}|[/]{2})[ ]*[0-9]{1,}[ ]*[=]{1}", s):
        l = re.split("([+\-*%/=])", s)
        if l[1] == "/":
            x, y, o = int(l[0]), int(l[4]), "//"
        else:
            x, y, o = int(l[0]), int(l[2]), l[1]
        if o == "+":
            return x + y
        elif o == "-":
            return x - y
        elif o == "*":
            return x * y
        elif o == "%":
            return x % y
        elif o == "//":
            return x // y
        else:
            print("Oops, something weird happened :(")

    else:
        print("Oops, operation not accepted")


if __name__ == "__main__":
    print(calculator())
