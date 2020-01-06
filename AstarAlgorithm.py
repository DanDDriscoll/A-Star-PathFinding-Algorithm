import math
import numpy as np

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.neighbors = []
        self.value = 1

    def add_neighbors(self, grid):
        position = self.position
        for neighbor_positions in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]:
            neighbor_position = (position[0] + neighbor_positions[0], position[1] + neighbor_positions[1])
            if (len(grid)) > neighbor_position[0] >= 0 and (len(grid[0])) > neighbor_position[1] >= 0 and \
                    grid[neighbor_position[0]][neighbor_position[1]] != 1:
                neighbor = grid[neighbor_position[0]][neighbor_position[1]]
                self.neighbors.append(neighbor)


def heuristic(node, goal):
    d = math.sqrt((node.position[0] - goal.position[0]) ** 2 + (node.position[1] - goal.position[1]) ** 2)
    return d


def astar(start, goal):
    start_node = start
    goal_node = goal
    frontier.append(start_node)

    while len(frontier) > 0:
        curr_node = frontier[0]
        curr_index = 0
        for index, item in enumerate(frontier):
            if item.f < curr_node.f:
                curr_node = item
                curr_index = index
        frontier.pop(curr_index)
        closed_set.append(curr_node)
        if curr_node == goal_node:
            path = []
            current = curr_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # returns path list reversed giving correct path.
        for neighbor in curr_node.neighbors:
            new_path = False
            if neighbor not in closed_set:
                temp_g = curr_node.g + heuristic(curr_node, neighbor)  # cost
                if neighbor in frontier:
                    if temp_g < neighbor.g:
                        new_path = True
                        neighbor.g = temp_g
                else:
                    new_path = True
                    neighbor.g = temp_g
                    frontier.append(neighbor)
                if new_path:
                    neighbor.h = heuristic(neighbor, goal_node)
                    neighbor.f = neighbor.h + neighbor.g
                    neighbor.parent = curr_node


frontier = []
closed_set = []


def main():
    col_len = 10
    row_len = 10
    grid = [[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(col_len):
        for j in range(row_len):
            if grid[i][j] != 1:
                grid[i][j] = Node(None, (i, j))

    for i in range(col_len):
        for j in range(row_len):
            if type(grid[i][j]) == Node:
                grid[i][j].add_neighbors(grid)

    path = astar(grid[0][0], grid[len(grid) - 1][len(grid) - 1])
    print(path)
    grid = [[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for x, y in path:
        grid[x][y] = '>'

    print(np.array(grid))

    # col_len = 10
    # row_len = 10
    # grid = [0 for i in range(col_len)]
    # for i in range(col_len):
    #     grid[i] = [0 for i in range(row_len)]
    # print('\n'.join([''.join(['{:4}'.format(item) for item in rows])
    #                  for rows in grid]))
    # for i in range(col_len-1):
    #     grid[i][5] = 1
    # print()
    # print('\n'.join([''.join(['{:4}'.format(item) for item in rows])
    #                  for rows in grid]))
    # for i in range(col_len):
    #     for j in range(row_len):
    #         if grid[i][j] != 1:
    #             grid[i][j] = Node(None, (i, j))
    #
    # for i in range(col_len):
    #     for j in range(row_len):
    #         if type(grid[i][j]) == Node:
    #             grid[i][j].add_neighbors(grid)
    #
    # path = astar(grid[0][0], grid[len(grid) - 1][len(grid) - 1])
    # print(path)

    # col_len = 10
    # row_len = 10
    # grid = [[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #
    # for i in range(col_len):
    #     for j in range(row_len):
    #         if grid[i][j] != 1:
    #             grid[i][j] = Node(None, (i, j))
    #
    # for i in range(col_len):
    #     for j in range(row_len):
    #         if type(grid[i][j]) == Node:
    #             grid[i][j].add_neighbors(grid)
    #
    # path = astar(grid[0][0], grid[len(grid) - 1][len(grid) - 1])
    # print(path)


if __name__ == '__main__':
    main()
