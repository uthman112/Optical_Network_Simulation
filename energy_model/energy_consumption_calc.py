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

        energy_per_bit=profiles[profile_name]['energy_per_bit_pj']
        power_watts= (traffic_gbps*1e9)*(energy_per_bit*1e-12)
        link_power_watts[links]=power_watts

    return link_power_watts