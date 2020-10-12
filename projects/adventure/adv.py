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
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

    def get_opposite(self):
        if self.direction == 'n':
            return 's'
        if self.direction == 's':
            return 'n'
        if self.direction == 'e':
            return 'w'
        if self.direction == 'w':
            return 'e'

def build_path():
    q = Stack()
    visited = set()

    sub_path = []

    for direction in world.starting_room.get_exits():
        if direction == 'n' and world.starting_room.n_to not in visited:
            q.push(Node_And_Direction('n', world.starting_room))
            sub_path.append('n')

        if direction == 's' and world.starting_room.s_to not in visited:
            q.push(Node_And_Direction('s', world.starting_room))
            sub_path.append('s')

        if direction == 'w' and world.starting_room.w_to not in visited:
            q.push(Node_And_Direction('w', world.starting_room))
            sub_path.append('w')

        if direction == 'e' and world.starting_room.e_to not in visited:
            q.push(Node_And_Direction('e', world.starting_room))
            sub_path.append('e')

    while q.size() > 0:
        current_room = q.pop()
        visited.add(current_room.room)
        for direction in current_room.room.get_exits():
            if direction == 'n' and current_room.room.n_to not in visited:
                q.push(Node_And_Direction('n', current_room.room.n_to))
                traversal_path.append('n')

            if direction == 's' and current_room.room.s_to not in visited:
                q.push(Node_And_Direction('s', current_room.room.s_to))
                traversal_path.append('s')

            if direction == 'w' and current_room.room.w_to not in visited:
                q.push(Node_And_Direction('w', current_room.room.w_to))
                traversal_path.append('w')

            if direction == 'e' and current_room.room.e_to not in visited:
                q.push(Node_And_Direction('e', current_room.room.e_to))
                traversal_path.append('e')
            
# if at dead end (current room has all paths from it lead to already visited paths) 
# go and add oppisites of sub_path but backwards so that you get to start node
# then add directions again.               

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
