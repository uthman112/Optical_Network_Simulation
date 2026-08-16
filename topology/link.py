class link:
    def __init__(self, node_a, node_b, profile="fiber_default", capacity_gbps=100, distance_km=0.1):
        self.node_a=node_a
        self.node_b=node_b
        self.profile=profile
        self.capacity_gbps=capacity_gbps
        self.distance_km=distance_km
        self.active=True