import networkx as nx

def calc_shortest_path_using_djikstra(network_topology, source_node, target_node):
    network_graph=network_topology.graph
    return nx.shortest_path(network_graph, source=source_node, target=target_node)
