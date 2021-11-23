import doctest
import networkx as nx


def vcg_cheapest_path(graph, source, target):
    """


    >>> g = nx.Graph()
    >>> edges = [('a', 'b', 3), ('a', 'c', 5), ('a', 'd', 10), ('b', 'c', 1), ('b','d',4), ('c', 'd', 1)]
    >>> g.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(g, 'a', 'd')
    The edge ('a', 'b') pays: -4
    The edge ('a', 'c') pays: 0
    The edge ('a', 'd') pays: 0
    The edge ('b', 'c') pays: -2
    The edge ('b', 'd') pays: 0
    The edge ('c', 'd') pays: -3

    >>> vcg_cheapest_path(g,'b','c')
    The edge ('a', 'b') pays: 0
    The edge ('a', 'c') pays: 0
    The edge ('a', 'd') pays: 0
    The edge ('b', 'c') pays: -5
    The edge ('b', 'd') pays: 0
    The edge ('c', 'd') pays: 0

    >>> g2 = nx.Graph()
    >>> g2.add_nodes_from(range(1, 5))
    >>> g2.add_weighted_edges_from([(1, 2, 4), (1, 3, 5), (1, 4, 1),(2,4,3),(2,3,10),(3,4,2)])
    >>> vcg_cheapest_path(g2, 1, 4)
    The edge (1, 2) pays: 0
    The edge (1, 3) pays: 0
    The edge (1, 4) pays: -7
    The edge (2, 4) pays: 0
    The edge (2, 3) pays: 0
    The edge (3, 4) pays: 0

    >>> vcg_cheapest_path(g2, 3, 4)
    The edge (1, 2) pays: 0
    The edge (1, 3) pays: 0
    The edge (1, 4) pays: 0
    The edge (2, 4) pays: 0
    The edge (2, 3) pays: 0
    The edge (3, 4) pays: -6


    >>> vcg_cheapest_path(g2,1,6)
    Traceback (most recent call last):
    ...
    networkx.exception.NetworkXNoPath: No path to 6.

    >>> g3 = nx.Graph()
    >>> g3.add_nodes_from(range(1, 4))
    >>> g3.add_weighted_edges_from([(1, 2, 1), (1, 3, 2), (2, 3, 7)])

    >>> vcg_cheapest_path(g3, 1, 3)
    The edge (1, 2) pays: 0
    The edge (1, 3) pays: -8
    The edge (2, 3) pays: 0
    >>> g4 = nx.Graph()
    >>> g4.add_nodes_from(range(1, 4))
    >>> g4.add_weighted_edges_from([(1, 2, 5), (1, 3, 4), (2, 3, 8)])

    >>> vcg_cheapest_path(g4, 1, 3)
    The edge (1, 2) pays: 0
    The edge (1, 3) pays: -13
    The edge (2, 3) pays: 0
    >>> g5 = nx.Graph()
    >>> g5.add_nodes_from(range(1, 4))
    >>> g5.add_weighted_edges_from([(1, 2, 3), (1, 3, 6), (2, 3, 2)])

    >>> vcg_cheapest_path(g5, 1, 3)
    The edge (1, 2) pays: -4
    The edge (1, 3) pays: 0
    The edge (2, 3) pays: -3
    """
    shortest_dist, shortest_path = nx.single_source_dijkstra(graph, source, target)
    # path = (shortest_path,  shortest_path[i]) for i in range(1,len(shortest_path)-1)
    path = list(zip(shortest_path, shortest_path[1:]))
    for edge in graph.edges:
        copy_of_g = nx.Graph(graph)
        if edge in path:
            copy_of_g.remove_edge(edge[0], edge[1])
            print(
                f"The edge {edge} pays: {-nx.shortest_path_length(copy_of_g, source, target, 'weight') + shortest_dist - graph.edges[edge[0], edge[1]]['weight']}")
        else:
            print(f"The edge {edge} pays: 0")


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
