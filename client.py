import socket

my_socket = socket.socket()
my_socket.connect(('localhost', 8000))

msg = input(str("Please enter a message: "))

# msg = "Hi from Client | é | ü"

my_socket.send(msg.encode(encoding='utf_8'))
response = my_socket.recv(1024)

print(response)
my_socket.close()
