import sys

# read file
data = sys.stdin.readlines()

# clean
clean_data = [[int(i.strip()) for i in line.strip()] for line in data]

data = clean_data

# process
gamma, epsilon = [], []
ones, zeros = 0, 0

for i in range(len(data[0])):
    for j in data:
        if j[i] == 0:
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma.append("0")
        epsilon.append("1")

    else:
        gamma.append("1")
        epsilon.append("0")

    zeros, ones = 0, 0


gamma = int("".join(gamma), base=2)
epsilon = int("".join(epsilon), base=2)

print(gamma * epsilon)
