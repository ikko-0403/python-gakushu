import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 50007))
#     s.sendall(b'Helloooooooooooo')
#     data = s.recv(1024)
#     print(repr(data))

# ソケット作成（UDP）
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = 'Hello UDP Server!'
    s.sendto(message.encode(), ('127.0.0.1', 50007))

    data, addr = s.recvfrom(1024)
    print(f"サーバーからの応答: {data.decode()}")
