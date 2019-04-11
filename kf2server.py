from client import client
from server import GameServer
class kf2_server(GameServer):
    name = "Killing Floor 2"

    def __init__(self):
        self.name = "Brazen Floor 2"
        self.lgsm_name = "kf2server"
        self.ipaddr = "192.168.0.155"
        self.local_ipaddr = "192.168.0.155"

brazenfloor = kf2_server()
kf2_server.monitor(brazenfloor, "kf2server") #gross
