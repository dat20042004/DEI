# Phiên bản mô phỏng cực kỳ cơ bản
class ConsistentHashing:
    def __init__(self):
        self.servers = []
        
    def them_server(self, server_name):
        self.servers.append(hash(server_name))
        self.servers.sort() # Sắp xếp thành vòng tròn ảo
        
    def tim_server_cho_du_lieu(self, data_key):
        h = hash(data_key)
        for srv_hash in self.servers:
            if h <= srv_hash:
                return srv_hash
        return self.servers[0] # Vòng lại server đầu tiên