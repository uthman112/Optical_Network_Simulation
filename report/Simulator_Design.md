Say my network is a Data Center network 
I would be using with a Spine-Leaf topology(other options are fat tree, Clos, DragonFly)
The network would consist of the following objects, switch, link, server, traffic, routing algorithm, and energy model.
-----Each of those would be a python class
topology - (network.py, switch.py, link.py, server.py, topology_generator)
routing - (dijkstra.py, k_shortest.py, routing_base.py)
energy_model - (device_power.py, energy_calculator.py, cpo_model.py)
optimization - (energy_aware.py, traffic_optimizer.py)
experiments - (experiment_1.py,experiment_2.py)
figures - stores graphs
datasets - stores traffic matrices

