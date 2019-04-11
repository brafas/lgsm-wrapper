from client import client
from server import GameServer

NAME, IPADDR, LGSM_NAME = "Brazen Floor 2", "192.168.0.155", "kf2server"
class kf2_server(GameServer):
    # name = "Killing Floor 2"

    def __init__(self, name, ipaddr, lgsm_name):
        self.name = "Brazen Floor 2"
        self.ipaddr = "192.168.0.155"
        self.lgsm_name = "kf2server"
        #self.local_ipaddr = "192.168.0.155"

brazenfloor = kf2_server(NAME, IPADDR, LGSM_NAME)
kf2_server.monitor(brazenfloor, "kf2server") #gross

brazenfloor2 = GameServer("Brazen Floor 2", )
