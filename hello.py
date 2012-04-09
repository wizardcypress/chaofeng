from chaofeng import Frame, Server
import chaofeng.ascii as c

class Hello(Frame):

    def initialize(self):
        self.write('Hello,World!')
        self.close()

    def clear(self):
        self.write('Don leave me alone ...\n')

if __name__ == '__main__' :
    s = Server(Hello)
    s.run()