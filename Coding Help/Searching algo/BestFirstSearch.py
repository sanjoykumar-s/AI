from queue import PriorityQueue

# Graph and heuristic from your image
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'E': ['H', 'I'],
    'F': ['G'],
    'C': [],
    'D': [],
    'H': [],
    'I': [],
    'G': []
}

heuristic = {
    'S': 14,
    'A': 12,
    'B': 5,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'H': 4,
    'I': 9,
    'G': 0
}


def bestFirstSearch(start, goal):

    pq = PriorityQueue()
    pq.put((heuristic[start],start,[start]))
    open_set = {start}
    close_list = []

    step = 0

    while not pq.empty():

        f, current, path = pq.get()
        open_set.discard(current)
        close_list.append(current)

        print(f"\nStep : {step}: Visiting {current}")
        print(f"OPEN : ", list(open_set))
        print(f"CLOSE : ", close_list)

        if current == goal:
            print("\nFinal Path : " , "->".join(path))
            return path
        
        for neighbor in graph[current]:
            if neighbor not in close_list:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))
                open_set.add(neighbor)
        
        step += 1
    print("Goal is not reachable")



# Run the code
bestFirstSearch('S', 'G')