import socket
UDP_IP = "192.168.10.61"  # Replace with the IP address of the destination
UDP_PORT = 12000       # Replace with the port number of the destination
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    while True:
        message = input("Inserire un numero: ")
        try:
            int(message)
        except:
            continue

        message = f"/n{message}"
        break

    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(data.decode())

    risposta = input("Vuoi continuare?")
    if risposta.lower() != "si":
        break

# Close the socket
sock.close()