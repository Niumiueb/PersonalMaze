import tkinter as tk
from time import sleep
class Queue:
    def __init__(self , grid ,canvas,cell_size):
        self.grid = grid
        self.canvas = canvas
        self.cell_size = cell_size
        self.intersections= []
        self.visited=set()
        self.start = (3,0)
        self.end = (15,8)
        self.pointer = self.start
        self.all_the_intersections=[]
        self.finished = False
    def maze(self ):
        i, j = self.pointer
        self.visited.add(self.pointer)   
        neighbors = [ (i , j-1), (i , j+1),(i-1,j),(i+1,j)]
        whites = []
        print(f"Current position: {self.pointer} , intersections: {self.intersections}")
        self.mark_visited(self.pointer , "#5BC0BE")
        for ni , nj in neighbors:
            if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                if self.grid[ni][nj] == 0 and (ni, nj) not in self.visited:
                    whites.append((ni, nj))
                elif self.grid[ni][nj] == 2:  
                    print("Reached the end. ")
                    self.pointer = self.end
                    self.finished = True
                    return  
            else:
                continue  
        if len(whites) == 0 :
            self.pointer = self.intersections.pop()

        elif len(whites) == 1:
            self.pointer = whites[0]
        else:
            self.intersections.append(self.pointer)
            self.all_the_intersections.append(self.pointer)
            self.pointer = whites[0]
    def traverse(self):
        self.create_maze(self.grid, self.cell_size)
        self.animate_step()
    def animate_step(self):
        if not self.finished:
            self.maze()
            self.canvas.update()
            self.canvas.after(100 , self.animate_step)
        else :
            print("Finished")
            self.mark_visited(self.end , "#A40E4C")
    def mark_visited(self ,position,color):
        if position == self.start:
            color = "#A40E4C"
        i ,j = position
        self.canvas.create_rectangle(
                j * self.cell_size, i * self.cell_size, 
                (j + 1) * self.cell_size, (i + 1) * self.cell_size, 
                fill=color, outline="gray"
            )
    def create_maze(self,grid, cell_size=30):

        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    color = "white"  
                elif grid[i][j] == 1:
                    color = "#2C2C34"
                    
                elif grid[i][j]==2:
                    color="#A40E4C"
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
    [3, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0 ,0, 1, 1, 1, 1],
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

canvas = tk.Canvas(root, width=len(maze_grid[0]) * cell_size, height=len(maze_grid) * cell_size )
canvas.pack()

queue=Queue(maze_grid ,canvas,cell_size )  
intersections = queue.traverse()
print(f" These are the intersections: {intersections}")
root.mainloop()


