import socket

host = 'www.baidu.com'
port = 80
buf_size = 128
addr = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(addr)

while True:
    data = raw_input('>')
    if not data:
        break
    client.send(data)
    response = client.recv(4096)
client.close()
