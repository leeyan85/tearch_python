import socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client.connect(("127.0.0.1", 8000))

begin = 0

while True:
    msg = input(">>>").strip()
    if not msg:
        continue
    tcp_client.send(msg.encode('utf-8'))
    print("客户端已经发送消息")
    data = tcp_client.recv(1024)
    print("服务端发来的消息是", data.decode('utf-8'))