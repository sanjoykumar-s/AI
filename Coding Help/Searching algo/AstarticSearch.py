from queue import PriorityQueue

graph = {
    'S' : {'A':1, 'G':10},
    'A' : {'B':2, 'C':1},
    'C' : {'G':4, 'D':3},
    'D' : {'G':2},
    'B' : {'D':5},
    'G' : {}
}

huristic = {
    'S' : 5,
    'A' : 3,
    'B' : 4,
    'C' : 2,
    'D' : 6,
    'G' : 0
}

def a_star_search(start, goal):
    pq = PriorityQueue()
    pq.put((huristic[start], 0, start, [start]))
    open_list = {start}
    close_list = []

    step = 0

    while not pq.empty():
        f, g, current, path = pq.get()
        open_list.discard(current)
        close_list.append(current)

        print(f"\nStep={step}: Visiting {current}")
        print(f"OPEN:", list(open_list))
        print(f"CLOSE:", close_list)

        if current == goal:
            print("\nFinal Path", "->".join(path))
            print("Total Cost (F):" , f)
            return path, f
    
        for neighbor, cost in graph[current].items():
            if neighbor not in close_list:
                g_new = g + cost
                f_new = g_new + huristic[neighbor]
                pq.put((f_new,g_new,neighbor,path + [neighbor]))
                open_list.add(neighbor)

        step += 1
    
    print("Goal not reachable.")
    return None, float('inf')


a_star_search('S', 'G')

