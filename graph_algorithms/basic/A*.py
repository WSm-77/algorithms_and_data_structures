from typing import Tuple, Callable

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
INF = float("inf")

class Maze:
    def __init__(self, height, width, walls):
        self.width = width
        self.height = height
        self.walls = walls

def get_path(target, parents):
    path = []

    node = target

    while node is not None:
        path.append(node)
        node = parents[node]

    path.reverse()

    return path

def a_star(maze: Maze, source: Tuple[int, int], target: Tuple[int, int], heuristic: Callable[[Tuple[int, int]], int]):
    visited = set()
    distance = {source: 0}
    parents = {source: None}
    to_visit = {source}

    node = None

    while node != target:
        if not to_visit:
            return [], []

        min_cost = INF
        next_node = None
        for potential_next_node in to_visit:
            if min_cost == INF or distance[potential_next_node] + heuristic(potential_next_node) < min_cost:
                next_node = potential_next_node
                min_cost = distance[potential_next_node] + heuristic(potential_next_node)

        if next_node is None:
            return [], []

        # update current node
        node = next_node

        # handle node visit
        to_visit.remove(node)
        visited.add(node)

        # update to_visit
        x, y = node
        for dx, dy in MOVES:
            if 0 <= x + dx < maze.height and 0 <= y + dy < maze.width:
                new_node = (x + dx, y + dy)
                if new_node in visited or new_node in maze.walls:
                    continue

                to_visit.add(new_node)
                distance[new_node] = distance[node] + 1
                parents[new_node] = node

        print()
        draw_maze(maze, source, target, visited)

    return get_path(target, parents), visited

def draw_maze(maze: Maze, start=None, goal=None, path=None):
    """
    Draws the maze in the terminal using ASCII characters.

    Args:
        maze (Maze): maze object
        start (tuple): optional (row, col) start position
        goal (tuple): optional (row, col) goal position
        path (set): optional set of (row, col) tuples representing the path
    """
    for r in range(maze.height):
        row_str = ""
        for c in range(maze.width):
            pos = (r, c)
            if pos == start:
                row_str += "S"
            elif pos == goal:
                row_str += "G"
            elif path and pos in path:
                row_str += "*"
            elif pos in maze.walls:
                row_str += "#"
            else:
                row_str += "."
        print(row_str)

def parse_maze(maze_str: str) -> Maze:
    """
    Parses a maze string into a dictionary with size and walls.

    Args:
        maze_str (str): Multi-line string representation of the maze.

    Returns:
        Dict[str, Tuple[int, int]]: Dictionary with 'size' and 'walls'.
    """
    lines = list(filter(lambda x: x != '', map(str.strip, maze_str.splitlines())))
    walls = {(r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == '#'}
    return Maze(len(lines), len(lines[0]), walls)

if __name__ == "__main__":
    maze1 = """
        .###.
        .....
        .###.
        .###.
        .###.

        """

    maze2 = """
        .###...
        .....#.
        .###.#.
        .#...#.
        .#.###.
        .#.....
        """

    for id, maze in enumerate([maze1, maze2]):
        print(f"\n\n######## maze {id + 1} ########\n\n")

        maze_parsed = parse_maze(maze)
        source = (0, 0)
        target = (maze_parsed.height - 1, maze_parsed.width - 1)
        draw_maze(maze_parsed, start=source, goal=target)

        heuristic = lambda x: abs(target[0] - x[0]) + abs(target[1] - x[1])
        path, visited = a_star(maze_parsed, source, target, heuristic)
        print(f"\npath:\n")
        draw_maze(maze_parsed, source, target, path)
