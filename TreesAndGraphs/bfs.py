
class Queue:
    def __init__(self):
        self.array = []
        self.size = 0

    def add(self, value):
        self.array.insert(0, value)
        self.size += 1
        # print(self.array)

    def out(self):
        self.size -= 1
        return self.array.pop()


def bfs(root_node, goal_value):

    path_queue = Queue()
    initial_path = [root_node]
    path_queue.add(initial_path)

    """Pop the next path list off the frontier
    Get the frontier node from the path list
    Check if the node value matches the goal value
    If there is a match, return the path to the current node"""
    while path_queue.size > 0:
        current_path = path_queue.out()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")
        if current_node.value == goal_value:
            return current_path
        
    """For each child of the current node
    Make a copy of the current path
    Add the child to the copy
    Append the updated path to the frontier"""
    return None