from client import client
#from server import GameServer


NAME, IPADDR, LGSM_NAME = "Brazen Floor 2", "192.168.0.155", "kf2server"


class GameServer: #The base class.
    # Server object
    # define the IPAddress, the name of the server (friendly) and the name LGSM uses.
    def __init__(self, name, ipaddr, lgsm_name):
        #properties to initialize an initial object.
        self.name = name
        self.ipaddr = ipaddr
        self.lgsm_name = lgsm_name
        #self.local_ipaddr = None
        #print(self.name)

    def isrunning(self, name):

        pass

    def monitor(self):
        #self.lgsm_name = "kf2server"
        #ipaddr = "192.168.0.155"
        # have each instance of a GameServer be able to "monitor".
        client.connect(self.ipaddr, username="kf2server", password="bonesniff")
        print("Client connected kf2server@", self.ipaddr)

        stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} monitor")
        for line in stdout:
            print('... ' + line.strip('\n'))
        client.close()

    def start(self):
        client.connect(self.ipaddr, username=self.lgsm_name, password="bonesniff")
        print("kf2server connected")
        stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} start")

class KillingFloor2_S(GameServer):

    name = "Brazen Floor 2"
    ip = "192.168.0.155"
    port = "27015"

    def start(self):
        client.connect(self.ipaddr, username="kf2server", password="bonesniff")
        stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} start")
        for line in stdout:
            print('... ' + line.strip('\n'))
        client.close()
        print("kf2 server started")

    def stop(self):
        client.connect(self.ipaddr, username="kf2server", password="bonesniff")
        stdin, stdout, stderr = client.exec_command(f"./{self.lgsm_name} stop")
        for line in stdout:
            print('... ' + line.strip('\n'))
        client.close()
        print("kf2 server stopped")

    # def start(self):
    #     client = client.R710_Ssh(self.lgsm_name).connect()

class Rust_S(GameServer):
    pass




# brazenfloor2 = GameServer(NAME, IPADDR, LGSM_NAME)

brazenfloor2 = KillingFloor2_S(NAME, IPADDR, LGSM_NAME)

brazenfloor2.start()
