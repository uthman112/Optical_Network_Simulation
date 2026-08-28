import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import pandas as pd
from collections import defaultdict
from routing.djikstra_route import calc_shortest_path_using_djikstra

dataset_path = os.path.join(base_dir, 'datasets', 'traffic_amount.ods')

#associate traffic to links
def load_traffic_data(filepath=dataset_path):
    link_bandwidth=pd.read_excel(filepath)
    source=[]; dest=[]; traffic_demand=[]
    for row in link_bandwidth.itertuples():
        src=row.source_node.lower()
        dst=row.dest_node.lower()
        ul_dl_traffic=int(row.amount_of_data_perdirection_Gbps)*2
        source.append(src); dest.append(dst); traffic_demand.append(ul_dl_traffic)
        return source, dest, traffic_demand

def calculate_link_traffic(network, source, dest, traffic_demand):
    link_traffic=defaultdict(int) #defaults to 0 for missing keys
    for src, dst, demand in zip(source, dest, traffic_demand):
        path = calc_shortest_path_using_djikstra(network, src, dst)
    for u, v in zip(path[:-1], path[1:]):#zip pairs two array by their index
            individual_links_in_route=tuple(sorted((u,v)))
            link_traffic[individual_links_in_route] += demand
    return path, link_traffic

