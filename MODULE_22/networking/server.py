import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
port = 12345

s.bind((HOST_NAME, port))

s.listen(4)

while True:
    cilent , address = s.accept()
    print(f"Got a connection from {address}")
    cilent.send(bytes("Thank you for connecting", "utf-8"))
    cilent.close()





