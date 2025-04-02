

def dfs(node):
    if node is None:
        return
    dfs(node.left)
    print(node.data)
    dfs(node.right)
