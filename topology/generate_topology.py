from topology.switch import NetworkSwitch
from topology.link import link
from topology.network import network
import networkx as nx



def generate_spine_leaf_topology(num_spine=2, num_leaf=4, spine_profile="pluggable_400G",leaf_profile="pluggable_400G"):
    net=network()
    spines = [NetworkSwitch(f'spine{i}', profile=spine_profile, role='spine') for i in range(num_spine)]
    leaves = [NetworkSwitch(f'leaf{i}', profile=leaf_profile, role='leaf') for i in range(num_leaf)]

    for s in spines:
        net.add_switch(s)
    for l in leaves:
        net.add_switch(l)

    for s in spines:
        for l in leaves:
            net.add_link(link(s.id, l.id))
    return net



    
    '''
    for node_id in my_net.graph.nodes():
        switch=my_net.get_switch(node_id)
        switch_index=[]
        if switch.role == 'leaf':
            switch_index.append(switch.id)
        else:
            continue
        print(switch_index)
        print(nx.shortest_path(my_net, source=switch_index[0], target=switch_index[-1]))
    '''
