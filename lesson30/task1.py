class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    def addLeftChild(self, value):
        if self.leftChild is None:
            self.leftChild = BinaryTree(value)
            return

        node = BinaryTree(value)
        temp = self.leftChild
        self.leftChild = node
        node.leftChild = temp

    def addRightChild(self, value):
        if self.rightChild is None:
            self.rightChild = BinaryTree(value)
            return

        node = BinaryTree(value)

        temp = self.rightChild
        self.rightChild = node
        node.rightChild = temp

    def addRightChildTree(self, tree):
        if self.rightChild is None:
            self.rightChild = tree
            return
        return None

    def addLeftChildTree(self, tree):
        if self.leftChild is None:
            self.leftChild = tree
            return
        return None

    def removeRightChildTree(self):
        self.rightChild = None
        return

    def removeLeftChildTree(self):
        self.leftChild = None
        return

    def __repr__(self):
        return str(self.value)

    def printTree(tree):
        children = [tree]
        levels = [0]
        while len(children) > 0:
            node = children.pop()
            level = levels.pop()
            print(" " * level * 2, node)

            if node.rightChild:
                rightChild = node.rightChild
                children.append(rightChild)
                levels.append(level + 1)

            if node.leftChild:
                leftChild = node.leftChild
                children.append(leftChild)
                levels.append(level + 1)


def printTree(tree, level=0):
    if tree:
        printTree(tree.leftChild, level + 1)
        print(" " * 4 * level + '-> ' + str(tree.value))
        printTree(tree.rightChild, level + 1)


root = BinaryTree(1)
root.addLeftChild(2)
root.addRightChild(3)
root.leftChild.addLeftChild(5)
printTree(root)

print("***")

root2 = BinaryTree(23)
root2.addLeftChild(213)
root2.addRightChild(33)
root2.leftChild.addLeftChild(15)
root2.leftChild.addRightChild(25)
printTree(root2)

print("***")
root.leftChild.leftChild.addRightChildTree(root2)
root.leftChild.leftChild.addLeftChildTree(root2)
printTree(root)

print("***")
root.leftChild.leftChild.removeRightChildTree()
printTree(root)
