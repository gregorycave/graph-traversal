# graph_traversal.py
# written by Gregory Cave on 25/11/2016
# developed in the Python 3.1 programming environment

def dfs(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            dfs(graph, vertex, visited)
    return visited
    
if __name__ == "__main__":
    GRAPH = { "A":["B","D","E"], "B":["A","C","D"], "C":["B","G"], "D":["A","B","E","F"], "E":["A","D"], "F":["D"], "G":["C"]}
    visitedList = []
    traversal = dfs(GRAPH, "A", visitedList)
    print( "Nodes visited in this order: {0}".format(traversal))
