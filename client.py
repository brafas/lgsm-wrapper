import base64
import paramiko
import traceback
import os

from paramiko import SSHClient

R710_IP = "192.168.0.155"
#Public key
SSH_KEY = paramiko.RSAKey(data=base64.b64decode(b'AAAAB3NzaC1yc2EAAAABJQAAAQEArhpylh4AEOrcg5RDHq8zHKZbxeWGJRX9GrlIjYFPyoME0DiFOA4lh/907GsRoB \
        /jp6dleGAl/I+74oQv+bgeGlrmnK+e8TpmjzPDSNCkFxYH5vFI38LTmjRcgJXd8kvDSrA7goPBk1bjLJ6o6wAWqfxQGTBktG6C2aPh/a \
        AGeVRNY6JNUut1fRhij5C8zXotndPvivIER0OidBmyTasRsFualAhz2UaF9LnWwDLKMhQJ2nhjdhy38bF2NNNdJdWHWetDhKRbiep1nN \
        n24Oh1J6iKs2P86AZq/+csO4b7EmqH8eRIwJ9iLoY+lZCjOZ82K7Esp4sxh5sSblWoxOpAfw=='))

def r710_ssh(cmd, username, password):
    #send a cmd, return stdout. or stderr.. Close connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_host_keys().add('games.brefend.com', 'ssh-rsa', SSH_KEY)
    #Connection
    client.connect(R710_IP, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(f"{cmd}")
    stdarr = [stdin, stdout, stderr]
    for line in stdout:
        print('... ' + line.strip('\n'))
    client.close()
    # make a ssh client instance
    # return output of a command given in arguments perhaps.

def r710_sftp():
    hostname = "192.168.0.155" #r710 server.
    username = "kf2server"
    password = "bonesniff"
    #load host keys
    host_keys = paramiko.util.load_host_keys(
        os.path.expanduser("~/.ssh/known_hosts")
    )
    if hostname in host_keys:
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]

    try:
        t = paramiko.Transport((hostname, 22))
        t.connect(hostkey, username, password)
        sftp = paramiko.SFTPClient.from_transport(t)
        dirlist = sftp.listdir(".")
        print(f"Dirlist: {dirlist}")
        t.close()

    except Exception as e:
        print("*** Caught exception: %s: %s" % (e.__class__, e))
        traceback.print_exc()
        try:
            t.close()
        except:
            pass
