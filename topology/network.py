import networkx as nx
class network:
    def __init__(self):
        self.graph=nx.graph()
    def add_switch(self,switch):
        self.graph.add_node(switch.id, obj=switch)
    def add_link(self, link):
        self.graph.add_edge(link.node_a, link.node_b, obj=link)
    def get_switch(self, switch_id):
        return self.graph.node[switch_id]['obj']
    def get_link(self, node_a, node_b):
        return self.graph.edge[node_a,node_b]['obj']
    def switches(self):
        return[data['obj'] for _, data in self.graph.node(data=True)]
    def links(self):
        return self