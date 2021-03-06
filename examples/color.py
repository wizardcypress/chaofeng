from chaofeng import Frame, Server
import chaofeng.ascii as c

class ColorFrame(Frame):

    def initialize(self):
        self.write('Welcome to the colorful life !')
        while self.read() != c.k_c_c :
            pass

    def get(self,data):
        if data == c.k_up : self.write( c.bg_white + c.red + 'Up' )
        if data == c.k_down : self.write( c.bg_black + c.green + 'Down')

    def clear(self):
        self.write(c.reset + 'Happy ending ...\r\n')

if __name__ == '__main__' :

    s = Server(ColorFrame)
    s.run()
