import socket

from MODULE_22.networking.server import HOST_NAME

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

s.connect((HOST_NAME, port))

msg = s.recv(100)

print(msg.decode('utf-8'))

