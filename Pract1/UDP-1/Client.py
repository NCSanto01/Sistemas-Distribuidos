import socket
import pickle
from sys import argv
import time

server_ip = argv[1]
port = str(argv[2])
client_id = argv[3]

print(server_ip)
print(port, type(port), len(port))
print(client_id)


id_encoded = pickle.dumps(str(client_id), 0)


# bytes_tx = pickle.dumps(msg_encoded, 0)

# Check if port is a number
while port.isnumeric() == False:
    port = input("Port must be numeric: ")

port = int(port)

server_address = (server_ip, port)


seconds = 10
# time.clock()

connection = True
elapsed = 0
socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while connection==True:
    connection = False
    msg = input("Input message: ")
    print("Waiting for server...")
    start = time.time()
    msg_encoded = pickle.dumps(msg, 0)
    array = [msg, str(client_id)]
    array_encoded = pickle.dumps(array, 0)
    while not connection:
        try:
            socket.sendto(array_encoded, server_address)
            bytes_rx = socket.recvfrom(1024)
            msg_received = pickle.loads(bytes_rx[0])
            connection = True
        except:
            connection = False
            time.sleep(1)
            elapsed = time.time() - start
            if elapsed > seconds:
                print("Server time out")
                break
        
    if connection == True:
        try:
            print("Response: ", msg_received, "\n")
            # socket.close()
        except:
            # socket.close()
            print("Error")
    if msg == "exit":
        socket.close()
        break

    