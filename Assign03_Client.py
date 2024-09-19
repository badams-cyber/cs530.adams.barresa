import socket, random, time
from datetime import datetime

client_id = str(random.randint(1, 100))  # Generate a unique client ID

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 8080)

# Register client
client_socket.sendto(f"R {client_id}".encode(), server_address)

with open(f'client_{client_id}.txt', 'a') as file:
    while True:
        message, _ = client_socket.recvfrom(1024)
        message = message.decode().strip()
        file.write(f"{datetime.now()} - Received: {message}\n")
        
        if random.randint(15, 90):
            break

# Unregister client
client_socket.sendto(f"U {client_id}".encode(), server_address)
client_socket.close()
