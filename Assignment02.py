import socket

# UDP Server


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('', 12345)
sock.bind(server_address)

while True:
    print('Waiting for a message...')
    data, address = sock.recvfrom(1024)
    print('Received message:', data.decode())

    # Echo the message back to the client
    sock.sendto(data, address)