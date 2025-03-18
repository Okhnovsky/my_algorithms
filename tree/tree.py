class NodeManyChild:

    def __init__(self, obj, children=None):
        self.obj = obj
        if children is not None:
            self.children = children
        else:
            self.children = []


class Node:

    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        right = right
