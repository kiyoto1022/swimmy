import socket
import random
import time


class Command:
    def __init__(self, command):
        self.value = command

    def is_connection_lost(self):
        if not self.value:
            return True
        return False


class Bot:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8888
        self.session = None
        self.active = True

    def run(self):
        self.__connect()
        self.__wait_for_command()

    def __call(self):
        try:
            self.session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.session.connect((self.ip, self.port))
            self.session.settimeout(3)
            return True
        except:
            pass

    def __kill(self):
        try:
            self.session.shutdown(socket.SHUT_RDWR)
            self.session.close()
        except:
            pass

    def __connect(self):
        search = True
        while search:
            for _ in range(15):
                if self.__call():
                    search = False
                    break
                self.__kill()
                time.sleep(random.randint(1, 5))
            time.sleep(random.randint(10, 15))

    def __wait_for_command(self):
        while self.active:
            try:
                cmd = Command(self.session.recv(1024))
                if cmd.is_connection_lost():
                    self.__connect()
                    continue
                print cmd.value
            except socket.timeout:
                pass
            except:
                self.__connect()
                continue


if __name__ == '__main__':
    Bot().run()
