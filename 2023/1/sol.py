def read_input(file):
    with open(file) as f:
        return f.readlines()


def get_first_and_last_numbers(line):
    left, right = 0, len(line) - 1
    line = list(line)
    number1 = number2 = None

    while number1 is None or number2 is None:
        if line[left].isdecimal():
            number1 = int(line[left])
        else:
            left += 1

        if line[right].isdecimal():
            number2 = int(line[right])
        else:
            right -= 1

    return number1, number2


counter = 0
lines = read_input("input2")

for line in lines:
    print(line)
    number1, number2 = get_first_and_last_numbers(line)
    number = int(f"{number1}{number2}")
    counter += number

print(counter)
