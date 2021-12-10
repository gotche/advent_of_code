import sys

# read file
data = sys.stdin.readlines()

# clean
game = [int(i) for i in data[0].split(",")]

i = 2
boards = []
board = []

while i < len(data):
    if data[i].strip():
        board.append([int(j) for j in data[i].split()])
    else:
        boards.append(list(board))
        board = []
    i += 1

# last board added
boards.append(list(board))

# process
rows = len(board)
cols = len(board[1])
number_of_boards = len(boards)

state = [[None] * rows * cols for i in range(number_of_boards)]


def process_board(number, boards, board_index):
    row, col = 0, 0

    for i in boards[board_index]:
        try:
            col = i.index(number)
            state[board_index][row * cols + col] = 1
            break
        except:
            pass
        row += 1


def is_winner(board_index):
    return check_row(board_index) or check_col(board_index)


def check_row(board_index):
    for i in range(0, cols * rows, cols):
        if all(state[board_index][i : i + cols]):
            return True
    else:
        return False


def check_col(board_index):
    for i in range(cols):
        for j in range(rows):
            if state[board_index][cols * i + rows * j] is None:
                return False

        else:
            return True


def calculate_winning_value(board_index, value):
    # sum of all umarked
    unmarked = 0
    for i in range(cols * rows):
        if state[board_index][i] is None:
            unmarked += boards[board_index][i // cols][i % cols]

    return unmarked * value


for number in game:
    won = False
    for index in range(len(boards)):
        process_board(number, boards, index)
        if is_winner(index):
            won = True
            print(calculate_winning_value(index, number))
            break

    if won:
        break
