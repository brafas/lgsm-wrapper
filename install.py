from client import client

stdin,stdout,stderr = client.exec_command('ls') #For now it's ls
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()
