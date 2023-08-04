import socket
import threading
import time

class TelnetServer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.timeout = 10
        self.command='' # 收到的命令

    def accept(self):
        client_socket, client_address = self.socket.accept()
        return client_socket, client_address

    def send(self, client_socket, message):
        client_socket.sendall(message.encode())

    def receive(self, client_socket):
        data = client_socket.recv(1024)
        return data.decode()

    def close(self, client_socket):
        client_socket.close()

    def run(self): # 线程执行方法
        while True:
            try:
                client_socket, client_address = self.accept()
                client_socket.settimeout(self.timeout) # comm timeout
                print("Received connection from", client_address)

                message = ''
                while True:
                    message += self.receive(client_socket)
                    if message.endswith('\n'):
                        message = message.strip()
                        print("Message: ", message)
                        # self.send(client_socket, f"Received your message: {message}\n")
                        self.command = message

                        if message == "quit" or message == "exit":
                            return
                        
                        message=''

                self.close(client_socket)
            except Exception as ex:
                print(ex)


if __name__ == "__main__":
    print('''
created by Bard with prompt: [写一个python类，实现telnet服务端]
https://bard.google.com/
'''    )
    
    server = TelnetServer("localhost", 8023)
    server.start() # 启动线程

    while True:
        if server.command:
            print(f"Executing COMMAND: {server.command}")
            server.command = ''
        else:
            time.sleep(1)


'''
* 对于Telnet协议的不严谨理解：跑在TCP上的7位ASCII码数据流
* 一个实用场景：利用telnet的通用性，实现命令机制，控制程序执行特定操作
* Python有Telnet客户端库telnetlib.Telnet
'''