import topology.generate_topology as generate_topology
import routing.djikstra_route as djikstra_route
import topology.visualizer as visualizer
import traffic.traffic_generator as generate_spine_leaf_traffic
import energy_model.energy_consumption_calc as energy_consumption_calculator_in_watts
import pandas as pd
from collections import defaultdict


#test modules
my_net = generate_topology.generate_spine_leaf_topology(2,4)
i=0
for node, data in my_net.graph.nodes(data=True):
    i+=1
'''
for node, data in my_net.graph.nodes(data=True):
    print(node, '-->', data)
for i, l in enumerate(my_net.links()):
    print(f"link{i}: connects {l.node_a} to {l.node_b}")
   
'''
switch_ids=list(my_net.graph.nodes)
#for node,data in my_net.graph.nodes(data=True):
#    switch_ids.append(node)
'''
print(switch_ids)
route=djikstra_route.calc_shortest_path_using_djikstra(my_net, switch_ids[2],switch_ids[-1])
print(route)
visualizer.visualize_topology(my_net)
'''
'''-----------------------------break--------------------------------------------------------'''


sources, dests, demands = generate_spine_leaf_traffic.load_traffic_data()

link_traffic = generate_spine_leaf_traffic.calculate_link_traffic(
    network=my_net, source=sources, dest=dests, traffic_demand=demands
)
print("\nAccumulated Link Traffic (Gbps):")
for link, traffic in link_traffic.items():
    print(f"Link {link}: {traffic} Gbps")


profiles=energy_consumption_calculator_in_watts.load_device_profiles()
link_power=energy_consumption_calculator_in_watts.calculate_per_link_energy(link_traffic, my_net, profiles)
single_switch_asic_power, total_network_asic_power=energy_consumption_calculator_in_watts.calculate_ASIC_baseline_power(my_net, profiles)
total_power_consumption_in_network= energy_consumption_calculator_in_watts.total_energy_consumption_in_network(link_traffic, my_net)



print("\nPer-Link Power Consumption (Watts):")
for link, power in link_power.items():
    print(f"Link {link}: {power:.4f} W")

print(f"\nASIC baseline power consumption for a single switch per Tbps is {single_switch_asic_power:.4f}W")
print(f"ASIC power consumption for all nodes in the netowrk is {total_network_asic_power:.4f}W")
print(f"\nTotal energy consumption in this spine-leaf topology with {i} nodes is {total_power_consumption_in_network:.4f}W")