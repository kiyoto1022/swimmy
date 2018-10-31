# -*- coding: utf-8 -*-
from cmd import Cmd
from c2server import C2Server


class Console(Cmd):
    ''' Command & Control Server Console '''
    prompt = "swimmy > "
    # http://www.patorjk.com/software/taag/#p=display&h=1&f=ANSI%20Shadow&t=Swimmy
    intro = '''
███████╗██╗    ██╗██╗███╗   ███╗███╗   ███╗██╗   ██╗
██╔════╝██║    ██║██║████╗ ████║████╗ ████║╚██╗ ██╔╝
███████╗██║ █╗ ██║██║██╔████╔██║██╔████╔██║ ╚████╔╝ 
╚════██║██║███╗██║██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝  
███████║╚███╔███╔╝██║██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║   
╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝                                                     
    '''

    def __init__(self):
        Cmd.__init__(self)
        self.c2server = C2Server()

    def do_setip(self, arg):
        args = arg.split()
        if not self.__check_args(args, 1): return
        self.c2server.ip = args[0]

    def help_setip(self):
        print "Description: Assign the IP to host the server\n\tUsage: setip [IP]\n"

    def do_setport(self, arg):
        args = arg.split()
        if not self.__check_args(args, 1): return
        self.c2server.port = eval(args[0])

    def help_setport(self):
        print "Description: Assign the port to host the server\n\tUsage: setport [PORT]\n"

    def do_server_start(self, arg):
        self.c2server.start()

    def help_server_start(self):
        print "Description: Start the server\n\tUsage: server_start\n"

    def do_server_stop(self, arg):
        pass

    def help_server_stop(self):
        print "Description: Stop the server\n\tUsage: server_stop\n"

    def do_sessions(self, arg):
        self.c2server.display()

    def help_sessions(self):
        print "Description: Display a list of connected bots\n\tUsage: sessions\n"

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def __check_args(self, args, num):
        if len(args) != num:
            print '[-] Error: This Function takes {} arguments ({} given)'.format(num, len(args))
            return
        return True
