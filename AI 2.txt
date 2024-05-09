# Implement A* algorithm for any game search problem.(8 puzzle problem)

# Define the goal state as a global constant
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def get_possible_moves(state):
    # Given a state, return a list of possible moves
    moves = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(new_state)
    return moves

def astar(start_state):
    # Priority queue to store states with their priorities
    frontier = [(0 + heuristic(start_state), start_state)]
    came_from = {}  # To store the parent of each state
    cost_so_far = {tuple(start_state): 0}  # Cost from start to current state

    while frontier:
        current_priority, current_state = frontier.pop(0)

        # If the current state is the goal state, reconstruct the path
        if current_state == GOAL_STATE:
            path = []
            while current_state != start_state:
                path.append(current_state)
                current_state = came_from[tuple(current_state)]
            path.append(start_state)
            path.reverse()
            return path

        for move in get_possible_moves(current_state):
            new_cost = cost_so_far[tuple(current_state)] + 1
            if tuple(move) not in cost_so_far or new_cost < cost_so_far[tuple(move)]:
                cost_so_far[tuple(move)] = new_cost
                priority = new_cost + heuristic(move)
                frontier.append((priority, move))
                came_from[tuple(move)] = current_state

        # Sort the frontier based on priority
        frontier.sort(key=lambda x: x[0])

    return None  # No solution found

def heuristic(state):
    # Manhattan distance heuristic
    distance = 0
    for i in range(1, 9):
        s_row, s_col = divmod(state.index(i), 3)
        g_row, g_col = divmod(GOAL_STATE.index(i), 3)
        distance += abs(s_row - g_row) + abs(s_col - g_col)
    return distance

def main():
    # Set initial state of the puzzle
    start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    path = astar(start_state)

    if path is None:
        print("No solution found")
    else:
        print("Solution:")
        for i, state in enumerate(path):
            print("Step", i + 1)
            print_state(state)

def print_state(state):
    # Print the state of the puzzle
    for i in range(3):
        print(state[i * 3:i * 3 + 3])

if __name__ == "__main__":
    main()
