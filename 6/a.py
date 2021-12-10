import sys
from collections import deque

# read file
data = sys.stdin.readlines()

# clean
initial_state = [int(i) for i in data[0].split(",")]

state = [0] * 9

for fish in initial_state:
    state[fish] += 1

state = deque(state)

# process
days = 0
while days < 80:
    today = state.popleft()
    newborns = today
    state[6] += today
    state.append(newborns)

    days += 1

print(sum(state))
