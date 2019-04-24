import re
import os
from client import r710_sftp_get

def find_setting(setting, setting_file):

    result = re.findall(r"^\w+", setting_file)
    print(result)



def mc_setting(setting, value):
    #file can be serverfiles/
    with open(os.getcwd() + "/mcsettings/server.properties") as s:
        result = re.findall(r"^pvp\w+", s)
        print(result)
        print(value)

def mc_setting_check(setting):
    #return all settings in server.properties
    serv_prop = r710_sftp_get(username="mcserver", password="bonesniff", filename="server.properties")

    text_file = serv_prop.decode()

    with open("server.properties.tmp", "r+") as f:
        filedata = f.read()

    print(text_file)

def mc_toggle_pvp():
    serv_prop = r710_sftp_get(username="mcserver", password="bonesniff", filename="server.properties")

    with open("server.properties.tmp", "r+") as f:
        filedata = f.read()

    filedata = filedata.replace('pvp=true', "pvp=false")

    with open('server.properties.out', 'w') as f:
        f.write(serv_prop)
