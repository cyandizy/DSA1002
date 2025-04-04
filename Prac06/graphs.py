import numpy as np
from dsa_linked_list import DSALinkedList
from queues_linked import Queue as DSAQueue
from stacks_linked import Stack as DSAStack
from operator import attrgetter

class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()

    def add_vertex(self, label):
        if len(label) < 1:
            print(f"Label is too short.")
            return

        node = DSAGraphNode(label)
        self.vertices.insert_last(node)

    def add_edge(self, label1, label2):
        node1 = self.get_vertex(label1)
        node2 = self.get_vertex(label2)

        if node1 is None or node2 is None:
            raise ValueError(f"One or both vertices do not exist.")        

        if not self.is_adjacent(label1, label2):
            node1.add_edge(node2)
            node2.add_edge(node1)
        else:
            print(f"Node ({label1}) and ({label2}) are already adjacent.")

    def has_vertex(self, label):
        return True if self.get_vertex(label) is not None else False

    def get_vertex_count(self):
        vertices = self.vertices.display()
        return len(vertices)

    def get_edge_count(self):
        count = 0
        current = self.vertices.head
        while current:
            node = current.get_value()
            count += node.get_edge_count()
            current = current.get_next()
        
        return count // 2

    def get_vertex(self, label):
        current = self.vertices.head
        while current:
            node = current.get_value() 

            if node.get_label() == label:
                return node

            current = current.get_next()
        return None

    def get_vertex_list(self):
        vertex_list = []
        current = self.vertices.head
        while current:
            node = current.get_value()
            vertex_list.append(node)

            current = current.get_next()

        return vertex_list

    def get_adjacent_list(self, label):
        node = self.get_vertex(label)
        return node.get_adjacent_list()

    def is_adjacent(self, label1, label2):
        label1_adjacent_list = [node.get_label() for node in self.get_adjacent_list(label1)]
        label2_adjacent_list = [node.get_label() for node in self.get_adjacent_list(label2)]
        if label2 in label1_adjacent_list and label1 in label2_adjacent_list:
            return True

        return False

    def display_as_list(self):
        current = self.vertices.head
        if current == None:
            print("Graph is empty.")
            return
        
        while current:
            node = current.get_value()
            vertex_label = node.get_label()
            adjacents = node.to_string()
            print(f"{vertex_label}: {adjacents}")
            current = current.get_next()

    def display_as_matrix(self):
        size = self.get_vertex_count()
        if size < 1:
            print("Graph is empty.")
            return
        
        matrix = np.zeros((size, size), int)

        vertex_label_list = [vertex.get_label() for vertex in self.get_vertex_list()]
        
        current = self.vertices.head
        while current:
            node = current.get_value()
            vertex_label = node.get_label()
            vertex_idx = vertex_label_list.index(vertex_label)

            adjacent_list = [adjacent.get_label() for adjacent in self.get_adjacent_list(vertex_label)]
            for adjacent in adjacent_list:
                adjacent_idx = vertex_label_list.index(adjacent)
                matrix[vertex_idx][adjacent_idx] = 1

            current = current.get_next()

        print("   " + " ".join([vertex[0] for vertex in vertex_label_list]))
        
        for vertex_label, row in zip(vertex_label_list, matrix):
            print(vertex_label[:2], end=" ")
            if len(vertex_label) == 1:
                print(" ", end="")
            for element in row:
                print(f"{element} ", end="")
            print()

    def breadth_first_search(self):
        traversal = DSAQueue()
        queue = DSAQueue()
        vertex_list = self.get_vertex_list()

        if len(vertex_list) < 1:
            print("Graph is empty.")
            return

        for vertex in vertex_list:
            vertex.clear_visited()
        
        current_vertex = vertex_list[0]
        current_vertex.set_visited()
        queue.enqueue(current_vertex)

        while not queue.is_empty():
            current_vertex = queue.dequeue()
            traversal.enqueue(current_vertex)

            adjacent_list = sorted(current_vertex.get_adjacent_list(), key=attrgetter("label"))
            for adjacent in adjacent_list:
                if not adjacent.get_visited():
                    adjacent.set_visited()
                    queue.enqueue(adjacent)

        print(f"BFS = ", end="")
        while not traversal.is_empty():
            print(f"{traversal.dequeue().get_label()} ", end="")
        print()

    def depth_first_search(self):
        traversal = DSAQueue()
        stack = DSAStack()

        vertex_list = self.get_vertex_list()
        if len(vertex_list) < 1:
            print("Graph is empty.")
            return
        
        for vertex in vertex_list:
            vertex.clear_visited()

        current_vertex =  vertex_list[0]
        current_vertex.set_visited()
        stack.push(current_vertex)

        while not stack.is_empty():
            current_vertex = stack.pop()
            traversal.enqueue(current_vertex)

            adjacent_list = sorted(current_vertex.get_adjacent_list(), key=attrgetter("label"), reverse=True)
            for adjacent in adjacent_list:
                if not adjacent.get_visited():
                    adjacent.set_visited()
                    stack.push(adjacent)

        print(f"DFS = ", end="")
        while not traversal.is_empty():
            print(f"{traversal.dequeue().get_label()} ", end="")
        print()

    def delete_node(self, label):
        node = self.get_vertex(label)
        if node is None:
            print(f"Vertex ({label}) is not on the graph.")
            return

        adjacent_list = node.get_adjacent_list().copy()
        for adjacent in adjacent_list:
            self.delete_edge(node.get_label(), adjacent.get_label())
        
        self.vertices.remove(node)
        if self.get_vertex(label) is None:
            print(f"Deleted vertex ({label}) and its link to adjacent vertices.")
        else:
            print(f"Error deleting vertex ({label}).")

    def delete_edge(self, label1, label2):
        node1 = self.get_vertex(label1)
        node2 = self.get_vertex(label2)

        if node1 is None or node2 is None:
            raise ValueError(f"One or both vertices do not exist.")

        if self.is_adjacent(label1, label2):
            node1.delete_edge(node2)
            node2.delete_edge(node1)
        else:
            print(f"Node ({label1}) and ({label2}) are not adjacent.")    
    

class DSAGraphNode:
    def __init__(self, label):
        self.label = label
        self.adjacent_list = DSALinkedList()
        self.visited = False

    def get_label(self):
        return self.label

    def get_adjacent_list(self):
        adjacent = [i for i in self.adjacent_list.display()]
        return adjacent

    def add_edge(self, vertex):
        self.adjacent_list.insert_last(vertex)

    def get_edge_count(self):
        count = 0
        current = self.adjacent_list.head
        while current:
            count += 1
            current = current.get_next()
        
        return count
    
    def delete_edge(self, vertex):
        self.adjacent_list.remove(vertex)
            
    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

    def get_visited(self):
        return self.visited

    def to_string(self):
        label_list = [adjacent.get_label() for adjacent in self.get_adjacent_list()]
        return "[" + ", ".join(label_list) + "]"

if __name__ == "__main__":
    graph = DSAGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")
    graph.add_edge("B", "E")
    graph.add_edge("E", "F")
    graph.add_edge("D", "F")
    graph.add_edge("E", "G")
    graph.add_edge("F", "G")
    graph.display_as_list()
    graph.display_as_matrix()
    graph.breadth_first_search()
    graph.depth_first_search()