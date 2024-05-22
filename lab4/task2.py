from collections import deque

def solve_puzzle(board):
    target_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    start_state = tuple(board)

    predecessors = {start_state: []}

    queue = deque([(start_state, [])])

    while queue:
        state, moves = queue.popleft()

        if list(state) == target_state:
            return moves

        zero_index = state.index(0)

        for move in get_possible_moves(zero_index, len(board)):
            new_state = list(state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state = tuple(new_state)


            if new_state not in predecessors:
                predecessors[new_state] = moves + [move + 1]
                queue.append((new_state, predecessors[new_state]))

    return []

def get_possible_moves(zero_index, board_size):
    moves = []
    row, col = zero_index // 4, zero_index % 4

    if row > 0:
        moves.append(zero_index - 4)

    if row < 3:
        moves.append(zero_index + 4)

    if col > 0:
        moves.append(zero_index - 1)

    if col < 3:
        moves.append(zero_index + 1)

    return moves

def print_board(board):
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        print(row)

puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]
solution = solve_puzzle(puzzle)

if not solution:
    print("Решения нет")
else:
    print("Последовательность движений для решения головоломки:")
    current_state = puzzle
    print_board(current_state)
    print()

    for move in solution:
        zero_index = current_state.index(0)
        move_index = move - 1
        current_state[zero_index], current_state[move_index] = current_state[move_index], current_state[zero_index]
        print(f"Передвинуть элемент {move} на пустое место")
        print_board(current_state)
        print()