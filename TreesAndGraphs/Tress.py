class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # reference to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship 
        print(f'Removing {child_node.value} from {self.value}')
        new_children = [node for node in self.children if node != child_node]
        self.children = new_children

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children



# root = TreeNode('Founder')
# child_a = TreeNode('VP of Bananas')
# child_b = TreeNode('Executive Assistant')
# child_c = TreeNode('Banana R & D')
 
# # adding children to the root
# root.add_child(child_a)
# root.add_child(child_b)
 
# # assigning child_c to child_a creates an additional level in the tree
# child_a.add_child(child_c)
 
# root.traverse()
