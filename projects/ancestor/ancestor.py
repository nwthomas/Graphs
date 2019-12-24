class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


def create_reverse_graph(ancestors):
    graph = {}
    for edge in ancestors:
        key = edge[1]
        if key in graph:
            graph[key].add(edge[0])
        else:
            graph[key] = set()
            graph[key].add(edge[0])
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = create_reverse_graph(ancestors)
    finished_paths = []
    final = []
    q = Queue()
    q.enqueue([starting_node])

    while q.size() > 0:
        current_path = q.dequeue()
        if current_path[len(current_path) - 1] in graph:
            for ancestor in graph[current_path[len(current_path) - 1]]:
                q.enqueue(current_path + [ancestor])
        else:
            finished_paths.append(current_path)

    if len(finished_paths) == 0:
        return -1

    for path in finished_paths:
        if len(path) > len(final):
            final = path
        elif len(path) == len(final) and path[len(path) - 1] < final[len(final) - 1]:
            final = path
        else:
            continue

    if final[len(final) - 1] == starting_node:
        return -1

    return final[len(final) - 1]
