from ast import Try
import socket
import subprocess
import sys
from datetime import datetime

#Limpar a tela
subprocess.call('clear', shell=True)

#Solicite por um Input
remoteServer = input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print um banner daora com informação do host que estamos prestes a scanear
print ("_" * 60)
print ("Por favor espere, estou scaneando h host local", remoteServerIP)
print ("_" * 60)

#Obseve a data e a hora que o scan começou
t1 = datetime.now()

#Usando a função range specify ports
#E também vamos lidar com o error

try:
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
 print ("You pressed Ctrl+C")
 sys.exit()

except socket.gaierror:
  print ("Hostname could not be resolved. Exiting")
  sys.exit()

except socket.error:
  print ("Couldn't connect to server")
  sys.exit()

#fazendo checagem da hora novamente
t2 = datetime.now()

#calculando a diferença de tempo 
total = t2 - t1

#printando a informação na tela
print ('Scanning Completed in in '), total