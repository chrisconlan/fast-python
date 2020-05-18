class Node(object):
    def __init__(value: int):
        self.value = value

class Edge(object):
    def __init__(node_a: Node, node_b: Node):
        self.node_a = node_a
        self.node_b = node_b

a_node = Node(26)
another_node = Node(66)
some_edge = Edge(a_node, another_node) 
...