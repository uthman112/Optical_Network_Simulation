import os
import sys
import yaml

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

profile_path=os.path.join(base_dir, 'datasets', 'device_profile.yaml')

def load_device_profiles(filepath=profile_path):
    with open(filepath, 'r') as device_profiles:
        return yaml.safe_load(device_profiles)

def calculate_per_link_energy(link_traffic, network, profiles):
    link_power_watts={}
    for links, traffic_gbps in link_traffic.items():
        node_a, node_b=links
        switch_a=network.get_switch(node_a)
        profile_name=switch_a.profile

        energy_per_bit_pj=profiles[profile_name]['energy_per_bit_pj']
        power_watts= (traffic_gbps*1e9)*(energy_per_bit_pj*1e-12) #joules per second
        link_power_watts[links]=power_watts

    return link_power_watts

def calculate_ASIC_baseline_power(network, profiles):
    asic_power = profiles['asic_baseline']['power_per_tbps_watts']
    total_network_asic_power = 0.0
    for node_id in network.graph.nodes():
        switch = network.get_switch(node_id)
        switch_profile = switch.profile
        port_bandwidth = profiles[switch_profile]['bandwidth_gbps']
        switch_power = (switch.port_count * port_bandwidth * 1e-3) * asic_power
        total_network_asic_power += switch_power
    return switch_power, total_network_asic_power

def total_energy_consumption_in_network(link_traffic, network):
    profiles=load_device_profiles()
    link_power=calculate_per_link_energy(link_traffic=link_traffic, network=network, profiles=profiles)
    total_transceiver_power = sum(link_power.values())
    switch_power,total_network_asic_power=calculate_ASIC_baseline_power(network=network, profiles=profiles)
    total_energy = total_transceiver_power + total_network_asic_power
    return total_energy