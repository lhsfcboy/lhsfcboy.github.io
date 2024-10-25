g = {
    "S":{
        "A":10,
    },
    "A":{
        "B":20,
    },
    "B":{
        "E":30,
        "C":1,
    },
    "C":{
        "A":1,
    },
    "E":{},
}
print(g)


import math
infi = math.inf
costs = {
    "A":10,
    "B":infi,
    "C":infi,
    "E":infi,
}

previous = {
    "A":"S",
    "B":None,
    "C":None,
    "E":None,
}

processed = []

def lowest_cost_node():
    target_node = None
    current_min_cost = infi
    for node in costs:
        if costs[node] < current_min_cost and node not in processed:
            target_node = node
            current_min_cost = costs[node]
    print(f"current lowest cost node is {target_node}")
    return target_node

current_node = lowest_cost_node()

while current_node is not None:
    current_node_cost = costs[current_node]         
    for neighbor_node, neighbor_cost in g[current_node].items():
        print(f"looking at the neighbor_node {neighbor_node}, neighbor_cost is {neighbor_cost}")
        
        new_cost = current_node_cost + neighbor_cost
        print(f"comparing new_cost {new_cost} with costs[neighbor_node] {costs[neighbor_node]}")
        if new_cost < costs[neighbor_node]:
            costs[neighbor_node] = new_cost
            previous[neighbor_node] = current_node
            print(costs)
            print(previous)

    processed.append(current_node)
    print(f"current_node {current_node} is processed")
    print(f"processed is {processed}")

    current_node = lowest_cost_node()


print("-"*20)
print(costs)
print(previous)    