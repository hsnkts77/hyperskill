msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6,
            msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0
result = 0


def check_user_input(x):
    x = str(x)
    f = ("0" + x.strip("-").rstrip(".0")).isdigit()
    try:
        int(x)
        return "int"
    except ValueError:
        try:
            float(x)
            if f:
                return "int"
            return "float"
        except ValueError:
            return "str"


def is_one_digit(v):
    if check_user_input(v) == "int" and -10 < int(float(v)) < 10:
        return True
    return False


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg = msg + msg_7
    if (v1 == "0" or v2 == "0" or v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:

    calc = input(msg_0)
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if check_user_input(x) == "str" or check_user_input(y) == "str":
        print(msg_1)
        continue
    if oper not in "-*+/":
        print(msg_2)
        continue

    check(x, y, oper)

    if oper == "/" and y == 0:
        print(msg_3)
        continue
    elif oper == "+":
        result = float(x) + float(y)
    elif oper == "*":
        result = float(x) * float(y)
    elif oper == "-":
        result = float(x) - float(y)
    elif oper == "/":
        try:
            result = float(x) / float(y)
        except:
            print(msg_3)
            continue

    if result == -5.0:
        result = 5.0

    print(result)

    while True:
        store = input(msg_4)
        if store == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(messages[msg_index])
                    if answer == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        memory = result
                        break
                    else:
                        continue
            else:
                memory = result
                break

            break

        elif store == "n":
            break
        elif store != "n":
            continue

    while True:
        continue_calc = input(msg_5)
        if continue_calc not in "yn":
            continue
        break

    if continue_calc == "y":
        continue
    elif continue_calc == "n":
        break
