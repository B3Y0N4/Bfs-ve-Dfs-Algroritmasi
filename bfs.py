graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # Gezilmiş  düğümlerin  listesi.
queue = []     #queue atanmasi

def bfs(visited, graph, node): #bfs Algorithmanin fonksiyonu
  visited.append(node)
  queue.append(node)

  while queue:   # Butün duğumleri gezmek için while dongusü  
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    #bfs Algorithmanin fonksiyonu çağrilmasi
