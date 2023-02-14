import socket
import pickle
from sys import argv

msg = "Hello, I'm the server"
bytes_tx = str.encode(msg)

server_ip = str(argv[1])
port = str(argv[2])

# Check if port is a number
while port.isnumeric() == False:
    port = input("Port must be numeric: ")

port = int(port)

# If port is not a valid number: print("Invalid port")
try:
    socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    socket.bind((server_ip, port))
    print("Server up and listening!")

    while True:
        bytes_rx = socket.recvfrom(1024)
        message = pickle.loads(bytes_rx[0])[0]
        client_id = pickle.loads(bytes_rx[0])[1]
        address = bytes_rx[1]
        print("\nConnection received.")
        print("Message received: ", str(message))
        print("Number of characters of message", len(message))
        print("Client Id: ", str(client_id))
        print("Client address: ", str(address), "\n")
        if str(message) == "exit":
            print("Received exit instruction.")
            print("Server shutting down")
            bytes_tx = pickle.dumps("Received exit instruction, shutting down server", 0)
            socket.sendto(bytes_tx, address)
            break
        else:
            bytes_tx = pickle.dumps(str(len(message)) + " characters received", 0)
            socket.sendto(bytes_tx, address)
except:
    print("Invalid Port")