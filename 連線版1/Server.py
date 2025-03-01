from ServerSetting import *
import socket

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #TCP
    server.bind((BIND_IP,BIND_PORT))
    server.listen(LISTEN_MAX_SOCKET)
    print(f"Listening on {BIND_IP}:{BIND_PORT}")
    print("Waiting for new connection...")

    player1_c,player1_addr = server.accept()
    print(f"Player 1 {player1_addr} Ready!")
    player1_c.send(str(1).encode())     #告訴他是黑棋

    player2_c,player2_addr = server.accept()
    print(f"Player 2 {player2_addr} Ready!")
    player2_c.send(str(2).encode())     #告訴他是白棋

    #雙方就緒
    player1_c.send(str(1).encode())
    player2_c.send(str(1).encode())

    running = True
    while running:
        #黑子先動
        try:
            data = player1_c.recv(2048)
            if not data:
                break
            player1_c.send(data)
            player2_c.send(data)
        except socket.error as e:
            print(e)
            break
        #白子
        try:
            data = player2_c.recv(2048)
            if not data:
                break
            player1_c.send(data)
            player2_c.send(data)
        except socket.error as e:
            print(e)
            break
    
    try:
        player1_c.close()
    except:
        pass
    try:
        player2_c.close()
    except:
        pass
    server.close()