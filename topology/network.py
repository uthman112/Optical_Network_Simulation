import networkx as nx
class network:
    def __init__(self):
        self.graph=nx.Graph()
    def add_switch(self,switch):
        self.graph.add_node(switch.id, obj=switch)
    def add_link(self, link):
        self.graph.add_edge(link.node_a, link.node_b, obj=link)
    def get_switch(self, switch_id):
        return self.graph.nodes[switch_id]['obj']
    def get_link(self, node_a, node_b):
        return self.graph.edges[node_a,node_b]['obj']
    def switches(self):
        return[data['obj'] for _, data in self.graph.nodes(data=True)]
    def links(self):
        return[data['obj'] for _, _, data in self.graph.edges(data=True)]