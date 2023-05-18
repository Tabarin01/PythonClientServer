import socket
UDP_IP = "192.168.10.61"
UDP_PORT = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nome = input("Inserire nome: ")
msg = f"/r{nome}"
sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print(data.decode())

# Close the socket
sock.close()