
def dfs(v, endV):
    discovered[v]=True
    if v = endV:
        found=True
    for each neighbour u of v: # This needs correction
        if discovered[u] = False:
            dfs(u, endV)
    completelyExplored[v]=True
    
if __name__ == "__main__":
    discovered = [[1], [2], [3], [4], [5]]
    explored = [[1], [2], [3], [4], [5]]
    found = False
    traversal = dfs(GRAPH, "A", visitedList)
    print( "Nodes visited in this order: {0}".format(traversal))
