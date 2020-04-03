# class Graph:
#
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
#
#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()
#
#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise ValueError("vertex does not exist")
#
#     def add_undirected_edge(self, v1, v2):
#         """
#         Add an undirected edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise ValueError("vertex does not exist")
#
#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         if vertex_id in self.vertices:
#             return self.vertices[vertex_id]
#         else:
#             raise ValueError("vertex does not exist")
#
#      def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         # Create a queue
#         q = Queue()
#         # Enqueue the starting vertex
#         q.enqueue(starting_vertex)
#         # Create a set to store visited vertices
#         visited = set()
#         # While the queue is not empty...
#         while q.size() > 0:
#             # Dequeue the first vertex
#             v = q.dequeue()
#             # Check if it's been visited
#             # If it hasn't been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Enqueue all it's neighbors
#                 for neighbor in self.get_neighbors(v):
#                     q.enqueue(neighbor)
#
#
#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         # Create a stack
#         s = Stack()
#         # Push the starting vertex
#         s.push(starting_vertex)
#         # Create a set to store visited vertices
#         visited = set()
#         # While the stack is not empty...
#         while s.size() > 0:
#             # Pop the first vertex
#             v = s.pop()
#             # Check if it's been visited
#             # If it hasn't been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Push all it's neighbors onto the stack
#                 for neighbor in self.get_neighbors(v):
#                     s.push(neighbor)



# ____________________________________________________________________________________________________________

#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         visited = set()
#         queue = Queue()
#
# ​
# queue.enqueue((starting_vertex, self.vertices[starting_vertex]))
# ​
# while queue.size():
#     vertex_id, vertex_set = queue.dequeue()
#     print(vertex_id)
#     for vertex in vertex_set:
#         if not vertex in visited:
#             visited.add(vertex)
#             queue.enqueue((vertex, self.vertices[vertex]))
# ​
#
# def dft(self, starting_vertex):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     """
#     visited = set()
#     stack = Stack()
#
# ​
# stack.push((starting_vertex, self.vertices[starting_vertex]))
# ​
# while stack.size():
#     vertex_id, vertex_set = stack.pop()
#     print(vertex_id)
#     for vertex in vertex_set:
#         if not vertex in visited:
#             visited.add(vertex)
#             stack.pus


# ____________________________________________________________________________________________________________

#     def dft_recursive(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
# ​
#         This should be done using recursion.
#         """
#         # Check if the node has been visited
#         # If not...
#         # Mark it as visited
#         # Call dft_recursive on each neighbor
#
# ​
#
# def bfs(self, starting_vertex, destination_vertex):
#     """
#     Return a list containing the shortest path from
#     starting_vertex to destination_vertex in
#     breath-first order.
#     """
#     # Create a queue
#     # Enqueue A PATH TO the starting vertex
#     # Create a set to store visited vertices
#     # While the queue is not empty...
#     # Dequeue the first PATH
#     # GRAB THE VERTEX FROM THE END OF THE PATH
#     # Check if it's been visited
#     # If it hasn't been visited...
#     # Mark it as visited
#     # CHECK IF IT'S THE TARGET
#     # IF SO, RETURN THE PATH
#     # Enqueue A PATH TO all it's neighbors
#     # MAKE A COPY OF THE PATH
#     # ENQUEUE THE COPY
