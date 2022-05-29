#DFS
def DFS(visited,graph,node):
    if node not in visited:
        visited.append(node)
        print(node)
        for i in graph[node]:
            DFS(visited,graph,i)

graph = {
    'R' : ['A','B'],
    'A' : ['C','D'],
    'B' : ['E','F'],
    'C' : [],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = []

DFS(visited,graph,'R')

# BFS
def BFS(visited,fring,graph,node):
    visited.append(node)
    fring.append(node)
    while fring:
        ele = fring.pop(0)
        print(ele)
        for i in graph[ele]:
            if i not in visited:
                visited.append(i)
                fring.append(i)

graph = {
    'R' : ['A','B'],
    'A' : ['C','D'],
    'B' : ['E','F'],
    'C' : [],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = []
fring = []

BFS(visited,fring,graph,'R')
