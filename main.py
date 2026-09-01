import topology.generate_topology as generate_topology
import routing.djikstra_route as djikstra_route
import topology.visualizer as visualizer
import traffic.traffic_generator as generate_spine_leaf_traffic
import energy_model.energy_consumption_calc as energy_consumption_calculator_in_watts
import pandas as pd


'''
for node, data in my_net.graph.nodes(data=True):
    print(node, '-->', data)
for i, l in enumerate(my_net.links()):
    print(f"link{i}: connects {l.node_a} to {l.node_b}")
   

switch_ids=list(my_net.graph.nodes)


    

#for node,data in my_net.graph.nodes(data=True):
#    switch_ids.append(node)

print(switch_ids)
route=djikstra_route.calc_shortest_path_using_djikstra(my_net, switch_ids[2],switch_ids[-1])
print(route)
visualizer.visualize_topology(my_net)
'''



'''-----------------------------break--------------------------------------------------------'''
optical_interconnects=['pluggable_400G', 'cpo_400G', 'pluggable_800G', 'cpo_800G']
optical_interconnects_and_total_power_consumed={}
for optical_interconnect_technologies in optical_interconnects:
    i=0
    my_net, link_traffic, link_power, single_switch_asic_power, total_network_asic_power, total_power_consumption_in_network=generate_topology.generate_topology_and_return_power_consumption('spine_leaf',2,4,optical_interconnect_technologies,50)
    print("\nAccumulated Link Traffic (Gbps):")
    for link, traffic in link_traffic.items():
        print(f"Link {link}: {traffic} Gbps")


    print("\nPer-Link Power Consumption (Watts):")
    for link, power in link_power.items():
        print(f"Link {link}: {power:.4f} W")
    for node, data in my_net.graph.nodes(data=True):
        i+=1
        switch=my_net.get_switch(node)
        switch_profile=switch.profile
    print(f"\nASIC baseline power consumption for a single switch per Tbps is {single_switch_asic_power:.4f}W")
    print(f"Baseline power consumption for all nodes in the netowrk is {total_network_asic_power:.4f}W")
    print(f"\nTotal energy consumption in this spine-leaf topology with {i} nodes utilizing {switch_profile} is {total_power_consumption_in_network:.4f}W")
    optical_interconnects_and_total_power_consumed[switch_profile]=round(total_power_consumption_in_network,4)
print(optical_interconnects_and_total_power_consumed)

df=pd.DataFrame(list(optical_interconnects_and_total_power_consumed.items))





