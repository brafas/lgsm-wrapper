from client import SSH_KEY
from client import r710_ssh
import paramiko

#from server import GameServer


NAME, IPADDR, LGSM_NAME = "Brazen Floor 2", "192.168.0.155", "kf2server"

class GameServer: #The base class.
    # Server object
    # Default address is always r710 for game servers
    ipaddr = "192.168.0.155"

    def __init__(self, name, ipaddr, lgsm_name):
        #properties to initialize an initial object.
        self.name = name
        self.lgsm_name = lgsm_name

    def start(self): #default start for any server
        client.connect(self.ipaddr, username=self.lgsm_name, password="bonesniff")
        print("kf2server connected")
        stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} start")
        for line in stdout:
            print('... ' + line.strip('\n'))
        client.close()

     # def stop(self):
     #    client.connect(self.ipaddr, username=self.lgsm_name, password="bonesniff")
     #    stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} stop")
     #    for line in stdout:
     #        print('... ' + line.strip('\n'))
     #    client.close()

class KillingFloor2_S(GameServer):

    lgsm_name = "kf2server" #Provides lgsm_name variable data instead of stating on instantiation.
    #ports = ["27015", "7777"]

    def __init__(self, name):
        self.name = name

    def start(self):
        stdarr = r710_ssh("./kf2server start")
        stdout = stdarr[1]

    #define a custom start function for different types of kf2 servers.

class Rust_S(GameServer):
    pass




# brazenfloor2 = GameServer(NAME, IPADDR, LGSM_NAME)

brazenfloor2 = KillingFloor2_S(name=NAME)

brazenfloor2.start()
