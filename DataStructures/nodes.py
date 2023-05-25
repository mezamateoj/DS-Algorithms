# Basic Node Implementation

class Nodes:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value

node_1 = Nodes('I am node 1')
node_2 = Nodes('I am node 2')
node_3 = Nodes('I am node 3')

node_1.set_link_node(node_3)
node_3.set_link_node(node_2)

# access data from nodes

# from node 1 get nodes 3 data
node_3_data = node_1.get_link_node().get_value()
print(node_3_data)

# from node 3 get nodes 2 data
node_2_data = node_3.get_link_node().get_value()
print(node_2_data)