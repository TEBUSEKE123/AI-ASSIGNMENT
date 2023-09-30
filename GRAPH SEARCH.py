import heapq
from collections import deque


class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


def depth_first_search(graph, start, goal):
    stack = [(start, [start])]
    explored = set()

    while stack:
        node, path = stack.pop()
        explored.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in explored:
                stack.append((neighbor, path + [neighbor]))

    return None


def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])
    explored = set()

    while queue:
        node, path = queue.popleft()
        explored.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in explored:
                queue.append((neighbor, path + [neighbor]))

    return None


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    explored = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in path:
                    new_cost = cost + edge_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None


def greedy_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    explored = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)

            for neighbor in graph[node]:
                if neighbor not in path:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None


def a_star_search(graph, start, goal, heuristic):
    priority_queue = [(0, start, [start])]
    explored = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in path:
                    g_cost = cost + edge_cost
                    f_cost = g_cost + heuristic[neighbor]
                    heapq.heappush(priority_queue, (f_cost, neighbor, path + [neighbor]))

    return None

graph = {
        'S': ['A', 'B'],
        'A': ['S', 'B', 'C'],
        'B': ['S', 'A', 'C'],
        'C': ['A', 'B', 'D', 'G'],
        'D': ['C', 'D', 'G'],
        'G': ['C', 'D']
    }

graph_cost = {
        'S' : {'A': 3, 'B': 1},
        'A' : {'B': 2, 'C': 2, 'S': 3},
        'B' : {'A': 2, 'C': 3, 'S': 1},
        'C' : {'A': 2, 'B': 3, 'D': 4, 'G': 4},
        'D' : {'C': 4, 'G': 1},
        'G' : {'D': 1, 'C': 4}

    }


heuristic = {
        'S': 7,
        'A': 5,
        'B': 7,
        'C': 4,
        'D': 1,
        'G': 0
    }

initial_state = 'S'
goal_state = 'G'

# Perform the search
dfs_result = depth_first_search(graph, initial_state, goal_state)
bfs_result = breadth_first_search(graph, initial_state, goal_state)
ucs_result = uniform_cost_search(graph_cost, initial_state, goal_state)
greedy_result = greedy_search(graph, initial_state, goal_state, heuristic)
astar_result = a_star_search(graph_cost, initial_state, goal_state, heuristic)

print("DFS result:", dfs_result)
print("BFS result:", bfs_result)
print("UCS result:", ucs_result)
print("Greedy result:", greedy_result)
print("A* result:", astar_result)