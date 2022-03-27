import pytest


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges


def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated


graph1 = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

@pytest.mark.parametrize('graph, start, end, expected', [
    (graph1, 'A', 'D', ['A', 'B', 'C', 'D']),
])
def test_first_path(graph, start, end, expected):
    assert find_path(graph, start, end) == expected

@pytest.mark.parametrize('graph, start, end, expected', [
    (graph1, 'A', 'D', [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]),
])
def test_all_paths(graph, start, end, expected):
    assert find_all_paths(graph, start, end) == expected

@pytest.mark.parametrize('graph, start, end, expected', [
    (graph1, 'A', 'D', ['A', 'B', 'D']),
])
def test_shortest_path(graph, start, end, expected):
    assert find_shortest_path(graph, start, end) == expected


graph2 = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }


@pytest.mark.parametrize('graph, expected', [
    (graph2, [('a', 'c'), ('b', 'c'), ('b', 'e'),
              ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'),
              ('d', 'c'), ('e', 'c'), ('e', 'b')]),
])
def test_edges(graph, expected):
    edges = generate_edges(graph)
    print(edges)
    assert generate_edges(graph) == expected


@pytest.mark.parametrize('graph, expected', [
    (graph2, ['f']),
])
def test_isolated_nodes(graph, expected):
    assert find_isolated_nodes(graph) == expected