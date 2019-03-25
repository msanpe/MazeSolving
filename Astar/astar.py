import numpy as np

## Implementation based on the pseudocode found at:
## https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

# Author: Miguel Sancho


class astar:
    def __init__(self, maze_width, maze_height, image_pixels):
        self.width = maze_width
        self.height = maze_height
        self.image_pixels = image_pixels

    def calculatePath(self, start, end):
        visited = set() # already evaluated
        to_evaluate = {start}
        came_from = {start: None} # the node with shortest path to each node
        cost_from_start = {start: 0} # g score
        cost_start_to_goal = {start: cost_from_start[start] + self.manhattan(start, end)} # f score

        while to_evaluate:
            current = min(to_evaluate, key=lambda x: cost_start_to_goal[x])
            if current == end:
                return self.construct_path(came_from, end) # found the exit!
            to_evaluate.remove(current)
            visited.add(current)
            for neighbour in self.find_neighbours(current):
                if neighbour in visited:
                    continue  # already evaluated

                t_cost_from_start = cost_from_start[current] + self.manhattan(current, neighbour)

                if neighbour not in to_evaluate:
                    to_evaluate.add(neighbour)
                elif t_cost_from_start >= cost_from_start.get(neighbour, np.inf):
                    continue

                came_from[neighbour] = current
                cost_from_start[neighbour] = t_cost_from_start
                cost_start_to_goal[neighbour] = t_cost_from_start + self.manhattan(neighbour, end)
        return False

    def construct_path(self, previous, current):
        path = []
        while current is not None:
            path.append(current)
            current = previous[current]
        return list(reversed(path))

    def check_valid(self, p):
        x,y = p
        if x < 0 or x > self.width or y < 0 or y > self.height: # out of bounds
            return False
        pixel = self.image_pixels[x,y]
        if pixel < 1: # wall
            return False
        return True


    def find_neighbours(self, p):
        x, y = p
        neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        return [p for p in neighbors if self.check_valid(p)]


    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
