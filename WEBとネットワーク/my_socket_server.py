import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             print('接続されました:', addr)
#             while True:
#                 data = conn.recv(1024)
#                 print('受信内容:', data.decode())
#                 if not data:
#                     break
#                 print('data: {}, addr: {}'.format(data, addr))
#                 conn.sendall(b'Received: ' + data)

# ソケット作成（UDP）
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    print('UDPサーバー起動中...')

    while True:
        data, addr = s.recvfrom(1024)
        print(f"受信: {data.decode()} from {addr}")

        reply = f"Received: {data.decode()}"
        s.sendto(reply.encode(), addr)
