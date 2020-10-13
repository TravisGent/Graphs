from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue  # These may come in handy

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # 14 moves 9 rooms for test_cross

#-------------------------- MY CODE START ----------------------------------

# def dft(self, starting_vertex):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     """
#     q = Stack()
#     visited = set()
# 
#     q.push(starting_vertex)
#     
#     while q.size() > 0:
#         v = q.pop()
#         if v not in visited:
#             print(v)
#             visited.add(v)
#             for neighbor in self.get_neighbors(v):
#                 q.push(neighbor)

class Node_And_Direction:
    def __init__(self, direction, room):
        self.direction = direction
        self.room = room

def get_opposite(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

def bfs(starting_vertex, stack):
    queue = Queue()
    queue_visited = set()

    queue.enqueue([starting_vertex])
    destination_vertex = stack.vertex_position(-1)
    
    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]

        if v not in queue_visited:
            if v.room.id == destination_vertex.room.id:
                return path
            queue_visited.add(v)

            for direction in v.room.get_exits():
                if v.room.get_room_in_direction(direction) not in queue_visited:
                    new_path = path + [Node_And_Direction(direction, v.room.get_room_in_direction(direction))]
                    queue.enqueue(new_path)

    return None

def build_path():
    stack = Stack()
    visited = set()
    current_room = None
    previous_room = None

    for direction in world.starting_room.get_exits():
        stack.push(Node_And_Direction(direction, world.starting_room))

    while stack.size() > 0:
        if current_room:
            previous_room = current_room

        current_room = stack.pop()
        if current_room.room not in visited:
            visited.add(current_room.room)

        if current_room.room.id == 234:
            i = 0

        if previous_room:
            for direction in previous_room.room.get_exits():
                if previous_room.room.get_room_in_direction(direction) == current_room.room:
                    traversal_path.append(direction)

        run_bfs = True

        for direction in current_room.room.get_exits():
            if current_room.room.get_room_in_direction(direction) not in visited:
                stack.push(Node_And_Direction(direction, current_room.room.get_room_in_direction(direction)))
                run_bfs = False

        if run_bfs and stack.size() > 0 and stack.vertex_position(-1).room not in visited:
            search_for_path = bfs(current_room, stack)
            i = 1
            while i < len(search_for_path):
                traversal_path.append(search_for_path[i].direction)
                i += 1


# do DFT for getting into the stack, then when hit dead end i.e. no more to go that are not in visited, then do a BFS with the starting destination being
# where the current node is, and the target destination being the next node in the stack
# 
# also make sure that I am appending the right directions to the array, not the directions that are only referenced, but not traveled.            

build_path()

print("!!!!!!!!!!!!!!!!!!!!!!!")
print(traversal_path)
print("!!!!!!!!!!!!!!!!!!!!!!!")

#------------------------------ MY CODE END ----------------------------------

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
