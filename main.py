import topology.generate_topology as generate_topology
import routing.djikstra_route as djikstra_route
import topology.visualizer as visualizer
import pandas as pd
from collections import defaultdict


#test modules
my_net = generate_topology.generate_spine_leaf_topology(2,4)
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
#associate traffic to links
link_bandwidth=pd.read_excel('datasets/traffic_amount.ods')
link_traffic=defaultdict(int) #defaults to 0 for missing keys
source=[]; dest=[]; traffic_demand=[]
for row in link_bandwidth.itertuples():
    src=row.source_node.lower()
    dst=row.dest_node.lower()
    ul_dl_traffic=int(row.amount_of_data_perdirection_Gbps)*2
    source.append(src); dest.append(dst); traffic_demand.append(ul_dl_traffic)
    #print(f"source_node: {row.source_node} dest: {row.dest_node} bandwidth: {row.amount_of_data_perdirection_Gbps}")
    path=djikstra_route.calc_shortest_path_using_djikstra(my_net, src, dst)
    print(path)
    for u, v in zip(path[:-1], path[1:]):#zip pairs two array by their index
        individual_links_in_route=tuple(sorted((u,v)))
        link_traffic[individual_links_in_route]+=ul_dl_traffic

print("Accumulated Link Traffic (Gbps):")
for link, traffic in link_traffic.items():
    print(f"Link {link}: {traffic} Gbps")
