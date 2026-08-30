import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from topology.switch import NetworkSwitch
from topology.link import link
from topology.network import network
import networkx as nx
import csv
import itertools
import pandas as pd

dataset_path = os.path.join(base_dir, 'datasets', 'traffic_amount.ods')

def generate_spine_leaf_topology(num_spine=2, num_leaf=4, spine_profile="pluggable_400G",leaf_profile="pluggable_400G", traffic_demand_gbps=50):
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

    #---write leaf-to-leaf traffic demand matric to traffic_amount.ods in dataset--
    leaf_ids = [f"Leaf{i}" for i in range(num_leaf)]
    rows = [{"source_node": src, "dest_node": dst, "amount_of_data_perdirection_Gbps": traffic_demand_gbps}
        for src, dst in itertools.combinations(leaf_ids, 2)
    ]
    
    df = pd.DataFrame(rows)
    df.to_excel(dataset_path, engine='odf', index=False)

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
