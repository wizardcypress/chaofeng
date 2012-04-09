from chaofeng.ascii import *

class NMenu:

    def __init__(self,frame,data,default_ord=0):
        '''
        data = ( ((x,y),value,[keymap]),[...] )
        '''
        self._data = data
        self._select = default_ord
        self.session = frame.session
        self.keymap = dict( (x[1][2],x[0]) for x in filter(lambda x:len(x[1])>2,enumerate(data)))
        self.session.push(move2(*self._data[self._select][0])+'>')

    def fetch(self):
        return self._data[self._select][1]

    def send(self,data):
        if data == k_down :
            if self._select+1 < len(self._data):
                self._select += 1
        elif data == k_up :
            if self._select > 0 :
                self._select -= 1
        elif data in self.keymap :
            self._select = self.keymap[data]
        else : return
        self.session.push(backspace*2+move2(*self._data[self._select][0])+'>')
        

class TextInput:
    
    def __init__(self,frame,max_len=100):
        self.session = frame.session
        self.buffer = ''
        self.buffer_size = max_len

    def _send(self,data):
        self.session.push(data)

    def fetch(self):
        res = self.buffer
        self.buffer = ''
        return res

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
                dd = movex(-1)
                self._send(dd+' '+dd)
                self.buffer = self.buffer[:-1]
            return
        elif ord(c) >= 32 and c != IAC:
            self.buffer += data
            self._send(data)
