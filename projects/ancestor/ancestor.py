
# print(test_ancestors[1]) # prints (2, 3)
# print(test_ancestors[1][1]) # prints 3
# print("---------")
# '''
#    10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# '''

# def earliest_ancestor(ancestors, starting_node, childLookUp=None, ancestorArray=None):
#     newArray = []
# 
#     if childLookUp is None:
#         childLookUp = starting_node
# 
#     if ancestorArray is None:
#         ancestorArray = ancestors
# 
#     for item in ancestorArray:
#         if childLookUp == item[1]:
#             newArray.append(item)
# 
#     for item in newArray:
#         childLookUp = item[0]
#         earliest_ancestor(ancestors, childLookUp)
# 
#     return newArray

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = []

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].append(v2)
        else:
            raise IndexError("nonexistant vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("nonexistant vertex")

    def earliest_ancestor(self, ancestors, starting_node=None):
        # this turns it into graph that has connections upwards
        newItemList = []
        for item in ancestors:
            if item[0] not in newItemList:
                newItemList.append(item[0])
            if item[1] not in newItemList:
                newItemList.append(item[1])
        for item in newItemList:
            self.add_vertex(item)
        for item in ancestors:
            self.add_edge(item[1], item[0])

        newVar = self.get_neighbors(starting_node)
        if newVar is not []:
            self.get_neighbors(newVar[0])


# newGraph = Graph()
# newGraph.add_vertex(1)
# newGraph.add_vertex(2)
# newGraph.add_vertex(3)
# newGraph.add_vertex(4)
# newGraph.add_vertex(5)
# newGraph.add_vertex(6)
# newGraph.add_vertex(7)
# newGraph.add_vertex(8)
# newGraph.add_vertex(9)
# newGraph.add_vertex(10)
# newGraph.add_vertex(11)

# newGraph.add_edge(1, 3)
# newGraph.add_edge(2, 3)
# newGraph.add_edge(3, 6)
# newGraph.add_edge(5, 6)
# newGraph.add_edge(5, 7)
# newGraph.add_edge(4, 5)
# newGraph.add_edge(4, 8)
# newGraph.add_edge(8, 9)
# newGraph.add_edge(11, 8)
# newGraph.add_edge(10, 1)

# '''
#    10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# '''

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

newGraph = Graph()
newGraph.earliest_ancestor(test_ancestors)
newVar = newGraph.get_neighbors(3)
print(newVar[0])

# {
#     1: {10, 3}, 
#     2: {3},
#     3: {1, 2, 6}, 
#     4: {8, 5},
#     5: {4, 6, 7}, 
#     6: {3, 5}, 
#     7: {5},
#     8: {9, 11, 4}, 
#     9: {8},
#     10: {1}, 
#     11: {8}
# }