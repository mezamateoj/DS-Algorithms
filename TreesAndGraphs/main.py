from Tress import TreeNode
from bfs import bfs

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.add_child = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.add_child = [my_wish, my_todo]
photos.add_child = [my_cat, my_dog]

print(sample_root_node.value)

# Change the 2nd argument below
goal_path = bfs(sample_root_node, "Home")

if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)