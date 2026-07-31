from switch import NetworkSwitch
from link import link
from network import network


def generate_spine_leaf_topology(num_spine=2, num_leaf=4, spine_profile="pluggable_100G",leaf_profile="pluggable_100G"):
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

if __name__ == "__main__":
    my_net = generate_spine_leaf_topology(2,4)
    for node, data in my_net.graph.nodes(data=True):
        print(node, '-->', data)
    for i, l in enumerate(my_net.links()):
        print(f"link{i}: connects {l.node_a} to {l.node_b}")
    