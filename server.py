import socket
#from flask_sqlalchemy import sqlalchemy

# Instance library
my_socket = socket.socket()
# establish connection
my_socket.bind(('localhost', 8000))
# quantity of request that our socket can handle
my_socket.listen(5)

while True:
    connection, addr = my_socket.accept()
    print("New connection established")
    print(addr)

    request = connection.recv(1024)
    print(request.decode('utf-8'))

    msg = "Hello from SERVER"

    connection.send(msg.encode())
    connection.close()
