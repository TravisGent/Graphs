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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = {}

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1][v2] = '?'


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("nonexistant vertex")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        visited = set()

        q.push(starting_vertex)
        
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)

newGraph = Graph()

def build_graph(graph):
    graph.add_vertex(player.current_room.id)
    for direction in player.current_room.get_exits():
        graph.add_edge(player.current_room.id, direction)
    x = 0
    while x == 0:
        reference = player.current_room.id

        if "n" in graph.vertices[reference] and graph.vertices[reference]['n'] is '?':
            graph.vertices[reference]['n'] = 'OK'
            traversal_path.append('n')
            player.travel('n')

            if not (player.current_room.id in graph.vertices):
                graph.add_vertex(player.current_room.id)
                for direction in player.current_room.get_exits():
                    graph.add_edge(player.current_room.id, direction)

        elif "s" in graph.vertices[reference] and graph.vertices[reference]['s'] is '?':
            graph.vertices[reference]['s'] = 'OK'
            traversal_path.append('s')
            player.travel('s')

            if not (player.current_room.id in graph.vertices):
                graph.add_vertex(player.current_room.id)
                for direction in player.current_room.get_exits():
                    graph.add_edge(player.current_room.id, direction)

        elif "w" in graph.vertices[reference] and graph.vertices[reference]['w'] is '?':
            graph.vertices[reference]['w'] = 'OK'
            traversal_path.append('w')
            player.travel('w')

            if not (player.current_room.id in graph.vertices):
                graph.add_vertex(player.current_room.id)
                for direction in player.current_room.get_exits():
                    graph.add_edge(player.current_room.id, direction)

        elif "e" in graph.vertices[reference] and graph.vertices[reference]['e'] is '?':
            graph.vertices[reference]['e'] = 'OK'
            traversal_path.append('e')
            player.travel('e')

            if not (player.current_room.id in graph.vertices):
                graph.add_vertex(player.current_room.id)
                for direction in player.current_room.get_exits():
                    graph.add_edge(player.current_room.id, direction)

        else:
            x = 1

#    q = Stack()
#    visited = set()
#
#    q.push(player.current_room.id)
#
#    while q.size() > 0:
#        v = q.pop()
#        if v not in visited:
#            visited.add(v)
#            newGraph.add_vertex(v)
#            for direction in player.current_room.get_exits():
#                newGraph.add_edge(v, direction)
#                player.travel(direction)
#                q.push(player.current_room.id)
                
build_graph(newGraph)

print("!!!!!!!!!!!!!!!!!!!!!!!")
print(newGraph.vertices)
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
