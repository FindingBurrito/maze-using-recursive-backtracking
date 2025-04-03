import random
import time


class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = [["#" for _ in range(size)] for _ in range(size)]
        self.start = (0, 0)
        self.end = (size - 1, size - 1)
        self.generate_maze()

    def generate_maze(self):
        self.grid[0][0] = "S"
        self.grid[self.size - 1][self.size - 1] = "E"
        stack = [(0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            moved = False

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == "#":
                    self.grid[nx - dx][ny - dy] = " "
                    self.grid[nx][ny] = " "
                    stack.append((nx, ny))
                    moved = True
                    break

            if not moved:
                stack.pop()

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def solve(self):
        stack = [self.start]
        visited = set()
        path = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y = stack.pop()
            if (x, y) == self.end:
                break
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] != "#" and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    path[(nx, ny)] = (x, y)

        x, y = self.end
        while (x, y) in path:
            x, y = path[(x, y)]
            if (x, y) != self.start:
                self.grid[x][y] = "."

    def run(self):
        print("Generated Maze:")
        self.display()
        time.sleep(1)
        print("\nSolving Maze...")
        self.solve()
        time.sleep(1)
        print("\nSolved Maze:")
        self.display()


if __name__ == "__main__":
    maze = Maze(15)
    maze.run()
