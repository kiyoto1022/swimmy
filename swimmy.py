# -*- coding: utf-8 -*-
from console import Console


class Swimmy(Console):
    ''' Botnet Tools '''
    def start(self):
        self.cmdloop()


if __name__ == '__main__':
    Swimmy().start()
