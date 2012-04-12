from chaofeng.ascii import *

class BaseUI:

    def __init__(self,frame,**kwarg):
        self.frame = frame

    def fetch(self):
        pass

    def send(self,data):
        pass

    def read(self,termitor=['\r\n','\n','\r\0']):
        f = self.frame
        data = f.read()
        while data not in termitor :
            for char in data:
                print ord(char),
            print
            self.send(data)
            data = f.read()
        return self.fetch()
             
class NMenu(BaseUI):

    def __init__(self,frame,data,default_ord=0):
        '''
        data = ( ((x,y),value,[keymap]),[...] )
        '''
        BaseUI.__init__(self,frame)
        self.data = data
        self.select = default_ord
        self.frame = frame
        self.keymap = dict( (x[1][2],x[0]) for x in filter(lambda x:len(x[1])>2,enumerate(data)))
        self.frame.write(move2(*self.data[self.select][0])+'>')

    def fetch(self):
        return self.data[self.select][1]

    def send(self,data):
        if data == k_down :
            if self.select+1 < len(self.data):
                self.select += 1
        elif data == k_up :
            if self.select > 0 :
                self.select -= 1
        elif data in self.keymap :
            self.select = self.keymap[data]
        else : return
        self.frame.write(backspace*2+move2(*self.data[self.select][0])+'>')
        

class TextInput(BaseUI):
    
    def __init__(self,frame,max_len=100):
        BaseUI.__init__(self,frame)
        self.buffer = []
        self.buffer_size = max_len

    def fetch(self):
        return ''.join(self.buffer).encode('gbk')

    def send(self,data):
        c = data[0]
        if c == theNULL: return
        # elif data == k_left :
        #     if self.insptr > 0:
        #         self.insptr -= 1
        #         self._send(movex_d)
        #     return
        # elif data == k_right:
        #     if self.insptr < len(self.buffer):
        #         self.insptr += 1
        #         self._send(movex_f)
        #     return
        elif data == k_backspace or data == k_del :
            if self.buffer :
                p = self.buffer.pop()
                if p >= u'\u4e00' and p <= u'\u9fa5' :
                    dd = movex(-2)
                    self.frame.write("%s  %s" % (dd,dd))
                else:
                    dd = movex(-1)
                    self.frame.write("%s %s" % (dd,dd))
            return
        elif ord(c) >= 32 and c != IAC:
            try:
                self.buffer.extend(list(data.decode('gbk')))
                print self.buffer
                self.frame.write(data)
            except UnicodeDecodeError:
                pass
