import base64
import paramiko
from paramiko import SSHClient

LOCAL_IP = "192.168.0.155"

SSH_KEY = paramiko.RSAKey(data=base64.b64decode(
    b'AAAAB3NzaC1yc2EAAAABJQAAAQEArhpylh4AEOrcg5RDHq8zHKZbxeWGJRX9GrlIjYFPyoME0DiFOA4lh/907GsRoB \
    /jp6dleGAl/I+74oQv+bgeGlrmnK+e8TpmjzPDSNCkFxYH5vFI38LTmjRcgJXd8kvDSrA7goPBk1bjLJ6o6wAWqfxQGTBktG6C2aPh/a \
    AGeVRNY6JNUut1fRhij5C8zXotndPvivIER0OidBmyTasRsFualAhz2UaF9LnWwDLKMhQJ2nhjdhy38bF2NNNdJdWHWetDhKRbiep1nN \
    n24Oh1J6iKs2P86AZq/+csO4b7EmqH8eRIwJ9iLoY+lZCjOZ82K7Esp4sxh5sSblWoxOpAfw=='))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.get_host_keys().add('games.brefend.com', 'ssh-rsa', SSH_KEY)
#client.connect(LOCAL_IP, username='kf2server', password='bonesniff')

# class R710_Ssh:
#     def __init__(self, lgsm_name):
#         self.lgsm_name = lgsm_name
#
#     def connect(self):
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client,.get_host_keys().add('games.brefend.com', 'ssh-rsa', SSH_KEY)
#         client.connect(LOCAL_IP, username=self.lgsm_name, password='bonesniff')
#
#     def disconnect(self):
#         client.close()


class R710_Lgsm(SSHClient):
    r710_ip = LOCAL_IP

    def connect(self):
        client = paramiko.SSHClient()

# return 3tuple of std.
        return stdin, stdout, stderr
    pass


def r710_ssh(cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_host_keys().add('games.brefend.com', 'ssh-rsa', SSH_KEY)
    #Connection
    client.connect(IPADDR, username="kf2server", password="bonesniff")
    stdin, stdout, stderr = client.exec_command(f"{cmd}")
    stdarr = [stdin, stdout, stderr]
    for line in stdout:
        print('... ' + line.strip('\n'))
    client.close()
    return stdarr
    # make a ssh client instance
    # return output of a command given in arguments perhaps.
