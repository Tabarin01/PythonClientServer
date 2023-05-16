import socket

UDP_IP = "192.168.10.61"  # Replace with the IP address of the destination
UDP_PORT = 12000  # Replace with the port number of the destination, uguali alle porte di servizio

while True:
    message = input("Inserire un numero: ")  # Replace with the message you want to send
    try:
        int(message)
    except:
        continue
    message = f"/n{message}"  # formattazione predefinita dell'input
    break


# Create a UDP socket
sock = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # la creazione della socket è uguale al server, ma non avendo il bind non diventa server

# Send the message
sock.sendto(
    message.encode(), (UDP_IP, UDP_PORT)
)  # comunicazione in tupla in modo da non essere modificata, comunica con l'ip e la porta

# Receiving message
data, addr = sock.recvfrom(1024)
print(data.decode())
# Close the socket
sock.close()
