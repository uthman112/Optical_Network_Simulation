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
import traffic.traffic_generator as generate_traffic_between_leaves
import energy_model.energy_consumption_calc as energy_consumption_calculator_in_watts


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


def change_switch_profiles(network, profile_intended):
    switch_ids=list(network.graph.nodes)
    for node_ids in switch_ids:
        switch=network.get_switch(node_ids)
        switch.profile=profile_intended

    return network


def generate_topology_and_return_power_consumption(topology_type='spine_leaf', num_of_spines=2, num_of_leaves=4, switch_profiles="pluggable_400G", traffic_band=50):
    if topology_type=='spine_leaf':
        my_net=generate_spine_leaf_topology(num_of_spines, num_of_leaves,spine_profile=switch_profiles, leaf_profile=switch_profiles, traffic_demand_gbps=traffic_band)
        sources, dests, demands = generate_traffic_between_leaves.load_traffic_data()
        link_traffic = generate_traffic_between_leaves.calculate_link_traffic(network=my_net, source=sources, dest=dests, traffic_demand=demands)   
        profiles=energy_consumption_calculator_in_watts.load_device_profiles()
        link_power=energy_consumption_calculator_in_watts.calculate_per_link_energy(link_traffic, my_net, profiles)
        single_switch_asic_power, total_network_asic_power=energy_consumption_calculator_in_watts.calculate_ASIC_baseline_power(my_net, profiles)
        total_power_consumption_in_network= energy_consumption_calculator_in_watts.total_energy_consumption_in_network(link_traffic, my_net)
        return my_net, link_traffic, link_power, single_switch_asic_power, total_network_asic_power, total_power_consumption_in_network

    
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
