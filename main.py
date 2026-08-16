import topology.generate_topology as generate_topology
import routing.djikstra_route as djikstra_route
import topology.visualizer as visualizer




my_net = generate_topology.generate_spine_leaf_topology(2,4)
for node, data in my_net.graph.nodes(data=True):
    print(node, '-->', data)
for i, l in enumerate(my_net.links()):
    print(f"link{i}: connects {l.node_a} to {l.node_b}")

switch_ids=list(my_net.graph.nodes)
#for node,data in my_net.graph.nodes(data=True):
#    switch_ids.append(node)

print(switch_ids)
route=djikstra_route.calc_shortests_path(my_net, switch_ids[2],switch_ids[-1])
print(route)

visualizer.visualize_topology(my_net)

