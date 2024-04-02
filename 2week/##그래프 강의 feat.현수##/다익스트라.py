import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    print(distances)
    distances[start] = 0

    q = []
    heapq.heappush(q, (distances[start], start))
    print(q)
 
    while q : 
        nowDis, nowNode = heapq.heappop(q)
        print(nowNode)
        print(nowDis)
        print(q)
        
        if nowDis < distances[nowNode]:
            continue
    
        for newNode, newDis in graph[nowNode].items() :
            dis = newDis + nowDis
            if dis < distances[newNode]:
                distances[newNode] = dis
                heapq.heappush(q,[dis,newNode])
    print(distances)
    
dijkstra(graph, 'A')
