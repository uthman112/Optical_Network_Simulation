import matplotlib.pyplot as plt
import networkx as nx
from topology.generate_topology import generate_spine_leaf_topology

def visualize_topology(net):
    spines = [s for s in net.switches() if s.role == 'spine']
    leaves = [s for s in net.switches() if s.role == 'leaf']


    pos={}
    
    for x,s in enumerate(spines):
        pos[s.id]=(x, 1)
    for x,l in enumerate(leaves):
        pos[l.id]=[x, 0]

    device_color=[]
    for node_id in net.graph.nodes():
        switch = net.get_switch(node_id)
        if switch.role == 'spine':
            device_color.append('skyblue')
        else:
            device_color.append('orange')
    nx.draw(net.graph, pos=pos, node_color=device_color, with_labels=True, node_size=1500)
    plt.show()
    return pos


