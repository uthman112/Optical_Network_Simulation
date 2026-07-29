class NetworkSwitch:
    def __init__(self, switch_id, profile="pluggable_100G", role=None):
        self.id = switch_id
        self.profile = profile
        self.role = role
        self.active = True

    def __repr__(self):
        return f"Switch({self.id}, profile={self.profile}, role={self.role}"