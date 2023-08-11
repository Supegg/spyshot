import os
import time
from command_via_telnet import TelnetServer

def main(server, interval = 1):
    '''
    server: 交互服务
    interval: 采样间隔
    '''
    last = time.time()
     # 采样间隔
    
    while True:
        try:
            if server.command == 'kill':
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'STOP Service')
                return
            
            if time.time() - last > interval:
                last = time.time()
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'hook.bat')
                os.system(r'hook.bat')
            time.sleep(0.1)
        except Exception as ex:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ex)


if __name__ == '__main__':
    host = "localhost"
    port = 8023
    server = TelnetServer(host, port)
    server.start()

    main(server)

