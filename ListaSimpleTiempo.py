import time
import random
import graphviz
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_recursive(node.left, data)
            else:
                node.left = TreeNode(data)
        elif data > node.data:
            if node.right:
                self._insert_recursive(node.right, data)
            else:
                node.right = TreeNode(data)

def load_data_to_binary_search_tree(data_source):
    start_time = time.time()
    binary_search_tree = BinarySearchTree()
    for _ in range(1000): 
        binary_search_tree.insert(random.randint(0, 100))
    end_time = time.time()
    execution_time = end_time - start_time
    return binary_search_tree, execution_time

def main():
    data_sources = ["Fuente1", "Fuente2", "Fuente3", "Fuente4", "Fuente5"]
    execution_times = []

    for source in data_sources:
        binary_search_tree, execution_time = load_data_to_binary_search_tree(source)
        execution_times.append(execution_time)
        print(f"Datos cargados desde {source} en {execution_time:.6f} segundos")

    dot = graphviz.Digraph()
    for i, source in enumerate(data_sources):
        dot.node(str(i), source)
    for i in range(len(data_sources) - 1):
        dot.edge(str(i), str(i + 1), label=f"{execution_times[i]:.6f} s")
    dot.render('execution_times_bst', format='png', cleanup=True)

if __name__ == "__main__":
    main()
