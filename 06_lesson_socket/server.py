from socket import *
back_log = 5
buffer_size = 1024
tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 8000))
tcp_server.listen(back_log)

while True:
    print("服务端开始运行了")
    conn, addr = tcp_server.accept()
    print((addr, conn))
    while True:
        message = conn.recv(buffer_size)
        if message:
            print("%s 客户端发来的messages是%s" % (addr, message.decode('utf-8')))
            conn.send(message.upper())
        else:
            break
    conn.close()

tcp_server.close()