class NetworkSwitch:
    def __init__(self, switch_id, profile="pluggable_400G", port_count=24, role=None):
        self.id = switch_id
        self.profile = profile
        self.port_count=port_count
        self.role = role
        self.active = True

    def __repr__(self):
        return f"Switch('{self.id}', profile='{self.profile}', port_count'{self.port_count}' role='{self.role}'"