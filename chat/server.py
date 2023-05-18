utenti = {}

def app(addr, msg):
    global utenti

    command = msg[0:2]
    payload = msg[2:]

    if command == "/r":
        utenti[payload] = addr
        for nome, addr in utenti.items():
            server_socket.sendto(f"Server: {payload} partecipa alla chat".encode(), addr)
        
    elif command == "/m":
        i = payload.find("\n")
        nome = payload[:i]
        messaggio = payload[i+1:]
        for nome, addr in utenti.items():
            server_socket.sendto(f"{nome}: {messaggio}".encode(), addr)
        
    elif command == "/l":
        # TODO leggere solo se non va in porto prima
        pass
    elif command == "/e":
        # TODO sloggare
        pass

    # return f"Siamo al numero: {utenti}"


import socket
UDP_IP_ADDRESS = "192.168.10.61"
UDP_PORT_NO = 12000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_STREAM
server_socket.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("UDP server up and listening")
while True:
    data, addr = server_socket.recvfrom(1024)
    print("Received message:", addr, data.decode())
    msg = data.decode()
    if (addr[0] == "192.168.10.202" or addr[0] == "192.168.10.61") and data.decode() == "quit":
        break
    resp = app(addr, msg)
    # server_socket.sendto(resp.encode(), addr)