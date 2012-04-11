from chaofeng import Frame, Server
from chaofeng import ascii as c
from chaofeng.ui import TextInput,NMenu
from chaofeng.g import static

z = 0

def check_username(data):
    return data == 'admin'

class Welcome(Frame):

    background = static['welcome']

    def initialize(self,data_list):
        self.write(self.background+c.move2(24,13))
        self.input = TextInput(self)
        self.flag = 0

    def get(self,data):
        self.input.send(data)
        if data[0] == c.k_enter_linux or data[0] == c.k_enter_window:
            if self.flag == 0 :
                if check_username(self.input.fetch()) :
                    self.write('\r\nPassword:')
                    self.flag = 1
                else :
                    self.write('Wrong Admin.\n')
                    self.close()
                return
            elif self.flag == 1 :
                if check_username(self.input.fetch()) :
                    self.goto(Main)
                else :
                    self.write('Wrong Password.\n')
                    self.close()
            
    def clear(self):
        pass

class Main(Frame):

    background = static['main']

    def initialize(self):
        print self.session
        self.write(self.background+c.move2(12,5))
        self.menu = NMenu(self,[
                ( (12,5),'Group','e'),
                ( (13,5),'Digest','d'),
                ( (14,5),'Favo','f'),
                ( (15,5),'Reco','r'),
                ( (16,5),'Mail','m'),
                ( (17,5),'Talk','t'),
                ])

    def get(self,data):
        self.menu.send(data)
        if data == c.k_c_c :
            print self.menu.fetch()
    
    def clear(self):
        pass

if __name__ == '__main__' :
    s = Server(Main)
    s.run()
