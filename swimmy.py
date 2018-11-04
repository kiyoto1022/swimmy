# -*- coding: utf-8 -*-
from console import Console


class Swimmy(Console):
    ''' Botnet Tools '''
    def start(self):
        self.cmdloop()


def main():
    Swimmy().start()


if __name__ == '__main__':
    main()
