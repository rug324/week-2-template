'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():
    """
    Returns a directed graph represented as a list of sets.
    """
    graph = [
        {1, 4},  # a -> b, e
        {2},     # b -> c
        {3, 4},  # c -> d, e
        {1},     # d -> b
        set()    # e -> (no outgoing edges)
    ]
    return graph

def part_2_graph():
    """
    Returns a directed graph represented as a list of lists.
    """
    graph = [
        [0, 1, 4],  # a -> a, b, e
        [2],     # b -> c
        [0, 3, 4],  # c -> a, d, e
        [],     # d -> (no outgoing edges)
        [3]       # e -> d
    ]
    return graph

def part_3_graph():
    """
    Returns a weighted directed graph represented as a list of dicts.
    """
    graph = [
        {0: 8, 1: 1, 4: 4},  # a -> a (8), b (1), e (4)
        {2: 3},              # b -> c (3)
        {0: 2, 4: 4},        # c -> a (2), e (4)
        {},                  # d -> (no outgoing edges)
        {}                   # e -> (no outgoing edges)
    ]
    return graph

def part_4_graph():
     """
    Returns a directed graph represented as a dict of sets.
    """
    graph = {
        0: {0, 1, 4},  # a -> a, b, e
        1: {2},     # b -> c
        2: {0},  # c -> a
        3: set(),     # d -> (no outgoing edges)
        4: set()    # e -> (no outgoing edges)
    }
    return graph

def part_5_graph():
    """
    Returns a weighted directed graph represented as a dict of dicts.
    """
    graph = {
        0: {1: 5},       # a -> b (5)
        1: {4: 3},       # b -> e (3)
        2: {},           # c -> (no outgoing edges)
        3: {},           # d -> (no outgoing edges)
        4: {0: 6, 1: 2}  # e -> a (6), b (2)
    }
    return graph
