from client import SSH_KEY
from client import r710_ssh

#from server import GameServer


NAME, IPADDR, LGSM_NAME = "Brazen Floor 2", "192.168.0.155", "kf2server"

class GameServer: #The base class.
    # Server object
    # Default address is always r710 for game servers
    # Classwide Variables:
    ipaddr = "192.168.0.155"

    def __init__(self, name, lgsm_name):
        #properties to initialize an initial object.
        self.name = name
        self.lgsm_name = lgsm_name

    def start(self): #default start for any server
        r710_ssh(f"./{self.lgsm_name} start", username=self.lgsm_name, password="bonesniff")

class KillingFloor2_S(GameServer):
    #classwide variables:
    # lgsm_name = "kf2server" #Provides lgsm_name variable data instead of stating on instantiation.
    #ports = ["27015", "7777"]

    def __init__(self, name):
        self.name = name

    def start(self):
        r710_ssh(f"./{lgsm_name} start")

    def stop(self):
        r710_ssh(f"./{lgsm_name} stop")

    #define a custom start function for different types of kf2 servers.

class Rust_S(GameServer):

    pass

class Minecraft_S(GameServer):

    pass

# brazenfloor2 = GameServer(NAME, IPADDR, LGSM_NAME)

#brazenfloor2 = KillingFloor2_S(name="Brazen Floor 2", lgsm_name="kf2server", level="KF-OUTPOST")
brazecraft = Minecraft_S(name="Brazecraft", lgsm_name="mcserver")

brazecraft.start()
