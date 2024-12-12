import tkinter as tk
from collections import deque

class BFS:
    def __init__(self, grid, canvas, cell_size):
        self.grid = grid
        self.canvas = canvas
        self.cell_size = cell_size
        self.start = (3, 0)
        self.end = (15, 8)
        self.visited = set()
        self.queue = deque([self.start])
        self.parent = {}  # To reconstruct the path
        self.finished = False

    def traverse(self):
        self.create_maze(self.grid, self.cell_size)
        self.animate_step()

    def animate_step(self):
        if self.queue and not self.finished:
            self.bfs_step()
            self.canvas.update()
            self.canvas.after(100, self.animate_step)
        elif self.finished:
            print("Finished")
            self.reconstruct_path()

    def bfs_step(self):
        if not self.queue:
            return

        current = self.queue.popleft()
        self.visited.add(current)

        if current == self.end:
            self.finished = True
            return

        i, j = current
        neighbors = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]

        for ni, nj in neighbors:
            if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                if self.grid[ni][nj] == 0 and (ni, nj) not in self.visited:
                    self.queue.append((ni, nj))
                    self.parent[(ni, nj)] = current
                    self.mark_visited((ni, nj), "#5BC0BE")
                elif self.grid[ni][nj] == 2:
                    self.parent[(ni, nj)] = current
                    self.finished = True
                    return

    def reconstruct_path(self):
        current = self.end
        while current in self.parent:
            self.mark_visited(current, "#A40E4C")
            current = self.parent[current]

    def mark_visited(self, position, color):
        if position == self.start:
            color = "#A40E4C"
        i, j = position
        self.canvas.create_rectangle(
            j * self.cell_size, i * self.cell_size,
            (j + 1) * self.cell_size, (i + 1) * self.cell_size,
            fill=color, outline="gray"
        )

    def create_maze(self, grid, cell_size=30):
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    color = "white"
                elif grid[i][j] == 1:
                    color = "#2C2C34"
                elif grid[i][j] == 2:
                    color = "#A40E4C"
                else:
                    color = "#A40E4C"
                self.canvas.create_rectangle(
                    j * cell_size, i * cell_size,
                    (j + 1) * cell_size, (i + 1) * cell_size,
                    fill=color, outline="gray"
                )

root = tk.Tk()
root.title("Maze")

cell_size = 30
maze_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [3, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
]

canvas = tk.Canvas(root, width=len(maze_grid[0]) * cell_size, height=len(maze_grid) * cell_size)
canvas.pack()

bfs = BFS(maze_grid, canvas, cell_size)
bfs.traverse()

root.mainloop()
