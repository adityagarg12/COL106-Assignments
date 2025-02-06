from stack import Stack
from exception import PathNotFoundException
from maze import *
class PacMan:
    def __init__(self, grid):
        self.navigator_maze = grid.grid_representation

    def find_path(self, start, end):
        rows = len(self.navigator_maze)
        cols = len(self.navigator_maze[0])
        
        # Stack for DFS
        paths = Stack()
        paths.push([start])
        
        # Set for visited cells to prevent revisiting
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # Check if start or end points are blocked
        if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException
        
        while paths.len():
            # Pop the current path
            path = paths.pop()
            (x, y) = path[-1]
            if visited[x][y]==True:
                continue
            # Mark the current cell as visited
            visited[x][y] = True
            
            # Check if we reached the goal
            if (x, y) == end:
                return path
            
            # Explore neighbors (up, down, left, right)
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                
                # Check bounds and validity
                if (
                    0 <= new_x < rows and
                    0 <= new_y < cols and
                    visited[new_x][new_y]==False and
                    self.navigator_maze[new_x][new_y] == 0
                ):
                    # Push the new path onto the stack
                    paths.push(path + [(new_x, new_y)])
        
        # If no path is found
        raise PathNotFoundException
# from maze import *
# from exception import *
# from stack import *
# class PacMan:
#     def __init__(self, grid : Maze) -> None:
#         ## DO NOT MODIFY THIS FUNCTION
#         self.navigator_maze = grid.grid_representation
#     def find_path(self, start, end):
#         # IMPLEMENT FUNCTION HERE
#         rows=len(self.navigator_maze)
#         cols=len(self.navigator_maze[0])
#         paths=Stack()
#         paths.push([start])
#         visited_cell=[]
#         if self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1:
#             raise PathNotFoundException 
#         while paths.len():
           
#             path=paths.pop()
#             (x,y)=path[-1]
#             visited_cell.append((x,y))
#             has_way=False
#             if (x,y)==end:
#                 return path
                
#             for change_in_x,change_in_y in [(0,1),(1,0),(-1,0),(0,-1)]:
#                 new_x,new_y=x+change_in_x,y+change_in_y
#                 if 0<=new_x<rows and 0<=new_y<cols and (new_x,new_y) not in visited_cell and self.navigator_maze[new_x][new_y]==0:
#                     paths.push((path+[(new_x,new_y)]))
#                     has_way=True
#             if not has_way:
#                 continue        
#         raise PathNotFoundException

# from maze import *
# from exception import *
# from stack import *

# class PacMan:
#     def __init__(self, grid: Maze) -> None:
#         ## DO NOT MODIFY THIS FUNCTION
#         self.navigator_maze = grid.grid_representation

#     def find_path(self, start, end):
#         def is_ok(x, y):
#             return (0 <= x < n) and (0 <= y < m) and self.navigator_maze[x][y] == 0
        
#         def run_fn(mat, start, end, path, visited, path_found):
#             stack = Stack()
#             stack.push((start, []))
            
#             directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
#             while not stack.is_empty():
#                 (current_pos, current_path) = stack.pop()
#                 x, y = current_pos
                
#                 if visited[x][y]:
#                     continue
                
#                 visited[x][y] = True
                
#                 if current_pos == end:
#                     path.extend(current_path + [current_pos])
#                     path_found[0] = True
#                     return
                
#                 for chx, chy in directions:
#                     new_x=x + chx
#                     new_y=y + chy
#                     if is_ok(new_x, new_y) and not visited[new_x][new_y]:
#                         stack.push(((new_x, new_y), current_path + [current_pos]))
            
#             path_found[0] = False


#         n = len(self.navigator_maze)
#         m = len(self.navigator_maze[0])
        
#         visited = [[False] * m for _ in range(n)]
#         path = []
#         path_found = [False]  
        
#         if (self.navigator_maze[start[0]][start[1]] == 1) or (self.navigator_maze[end[0]][end[1]] == 1):
#             raise PathNotFoundException
        
#         run_fn(self.navigator_maze, start, end, path, visited, path_found)
        
#         if not path_found[0]:
#             raise PathNotFoundException
        
#         return path
