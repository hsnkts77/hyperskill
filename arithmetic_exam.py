import random


def check_input(x):

    try:
        int(x)
        return True
    except ValueError:
        try:
            float(x)
            return True
        except ValueError:
            print("Incorrect format.")
            return False


def check_answer_format(x):

    try:
        int(x)
        return True
    except ValueError:
        print("Wrong format!Try again.")
        return False


def check_answer(x, y):

    if x == y:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False


def generate_task():

    x, y = random.sample(range(2, 10), 2)
    o = random.choice("*-+")
    operation = str(x) + " " + o + " " + str(y)

    return operation


def calculate(c):

    result = 0
    try:
        int(c)
        result = int(c) * int(c)
    except ValueError:
        x = int(c.split()[0])
        o = c.split()[1]
        y = int(c.split()[2])

        if o == "+":
            result = x + y
        elif o == "-":
            result = x - y
        elif o == "*":
            result = x * y

    return result


mark = 0
task_count = 0
task = ""
user_choice = ""
prg = ""
while task_count != 5:

    first = "1 - simple operations with numbers 2-9"
    second = "2 - integral squares of 11-29"

    print("Which level do you want? Enter a number:")
    print(first)
    print(second)

    user_choice = input()
    if user_choice not in "12":
        print("Incorrect format.")
        continue

    while task_count != 5:
        if user_choice == "1":
            prg = first
            task = generate_task()
        elif user_choice == "2":
            prg = second
            task = str(random.choice(range(11, 30)))
        task_result = calculate(task)

        while True:
            print(task)
            answer = input()
            if not check_answer_format(answer):
                continue
            task_count += 1
            if check_answer(int(answer), task_result):
                mark += 1
            break
    break

print(f"Your mark is {mark}/{task_count}. Would you like to save the result? Enter yes or no.")
if input() in "yesYESYes":
    name = input("What is your name?")
    save = f'{name}: {mark}/{task_count} in level {prg.replace(" - ", " (")}).'
    with open("results.txt", "a") as f:
        f.write(save)
    print('The results are saved in "results.txt".')
