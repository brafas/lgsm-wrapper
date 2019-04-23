from client import r710_ssh
from client import r710_sftp_get

#from server import GameServer


NAME, IPADDR, LGSM_NAME = "Brazen Floor 2", "192.168.0.155", "kf2server"

class GameServer: #The base class.
    # Server object
    # Default address is always r710 for game servers

    def __init__(self, name, lgsm_name):
        self.name = name
        self.lgsm_name = lgsm_name

    def start(self): #default start for any server
        r710_ssh(f"./{self.lgsm_name} start", username=self.lgsm_name, password="bonesniff")

    def stop(self):
        r710_ssh(f"./{self.lgsm_name} stop", username=self.lgsm_name, password="bonesniff")

class KillingFloor2_S(GameServer):
    #classwide variables:
    # lgsm_name = "kf2server" #Provides lgsm_name variable data instead of stating on instantiation.
    #ports = ["27015", "7777"]
    #define a custom start function for different types of kf2 servers.
    pass

class Rust_S(GameServer):

    pass

class Minecraft_S(GameServer):

    def check_settings(self):
        #grab the mc server.properties file. Print it.
        serv_prop = r710_sftp_get(username=self.lgsm_name, password="bonesniff", filename="server.properties")
        #print(serv_prop.name)

    pass

# brazenfloor2 = GameServer(NAME, IPADDR, LGSM_NAME)

#brazenfloor2 = KillingFloor2_S(name="Brazen Floor 2", lgsm_name="kf2server", level="KF-OUTPOST")
brazecraft = Minecraft_S(name="Brazecraft", lgsm_name="mcserver")

#brazecraft.start()
brazecraft.check_settings()
