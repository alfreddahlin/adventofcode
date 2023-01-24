import heapq


class Queue:
    def __init__(self):
        self.elements = []
        self.index = 0

    def not_empty(self) -> bool:
        return len(self.elements) != 0

    def push(self, priority, cost, item):
        heapq.heappush(self.elements, (priority, cost, self.index, item))
        self.index += 1

    def pop(self):
        _, cost, index, state = heapq.heappop(self.elements)
        return cost, state  # , index


def search(
    start,
    tree,
    get_neighbors,
    target=None,
    get_cost=lambda x, y: 1,
    get_cost_remaining=lambda x, y, z: 0,
    is_finished=lambda x, y, z: x == y,
):
    # queue represented as tuple with priority, cost and state
    queue = Queue()
    queue.push(priority=0, cost=0, item=start)
    seen = {start}
    while queue.not_empty():
        cost, state = queue.pop()
        if is_finished(state, target, tree):
            return cost
        neighbors = get_neighbors(state, tree)
        for neighbor in neighbors:
            if neighbor not in seen:
                neighbor_cost = cost + get_cost(state, neighbor)
                remaining_cost = get_cost_remaining(neighbor, target, tree)
                queue.push(
                    priority=neighbor_cost + remaining_cost,
                    cost=neighbor_cost,
                    item=neighbor,
                )
        seen.update(neighbors)
    return None
