class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        self.node = None

    def insert(self, new_val):
        # Doing recursively
        node = self.root

        if new_val == node.value:
            pass
        else:
            while node.left != None or node.right != None:
                if new_val < node.value:
                    if node.left != None:
                        node = node.left
                    else:
                        node.left = Node(new_val)
                        break
                else:
                    if node.right != None:
                        node = node.right
                    else:
                        node.right = Node(new_val)
                        break

            if node.left == None or node.right == None:
                if new_val < node.value:
                    node.left = Node(new_val)
                else:
                    node.right = Node(new_val)

    def search(self, find_val):
        # Doing recursively
        node = self.root

        if find_val == node.value:
            return True
        else:
            while node.left != None or node.right != None:
                if find_val == node.value:
                    return True
                elif (find_val < node.value):
                    if node.left != None:
                        node = node.left
                    else:
                        return False
                else:
                    if node.right != None:
                        node = node.right
                    else:
                        return False

            if node.left == None and node.right == None:
                if find_val == node.value:
                    return True
                else:
                    return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
