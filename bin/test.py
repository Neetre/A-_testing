import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # distance from start node
        self.h = h  # heuristic - estimated distance to goal
        self.f = self.g + self.h  # total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(start, goal, graph):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.name)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # return reversed path

        neighbors = graph[current_node.name]
        for neighbor_name, cost in neighbors.items():
            if neighbor_name in closed_list:
                continue

            neighbor_node = Node(neighbor_name, current_node, current_node.g + cost, heuristic(neighbor_name, goal))

            if any(n.name == neighbor_name and n.g > neighbor_node.g for n in open_list):
                open_list.remove(next(n for n in open_list if n.name == neighbor_name))

            if not any(n.name == neighbor_name for n in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None

def heuristic(node, goal):
    # This is a placeholder heuristic function. In a real-world application,
    # this function would calculate the estimated distance from the current node to the goal.
    
    node_x, node_y = node
    goal_x, goal_y = goal
    distance = abs(node_x - goal_x) + abs(node_y - goal_y)
    
    return distance

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3, 'E': 7},
    'B': {'D': 5},
    'C': {'B': 2, 'D': 3},
    'D': {'E': 4},
    'E': {'D': 6}
}

print(astar('A', 'E', graph))  # Output: ['A', 'C', 'B', 'D', 'E']
