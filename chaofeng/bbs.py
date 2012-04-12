import eventlet
from chaofeng import ascii

class GotoInterrupt(Exception):
    
    def __init__(self,to_where):
        self.to_where = to_where

class EndInterrupt(Exception): pass

class Frame:

    buffer_size = 1024
    
    g = {}

    def __init__(self,server,sock,session):
        self.session = session
        self.server = server
        self.sock = sock
        self.initialize()

    def initialize(self):
        pass

    def clear(self):
        pass

    get = None

    def read(self,buffer_size=1024):
        data = self.sock.recv(buffer_size)
        if not data :
            self.close()
        else:
            if self.get : self.get(data)
            return data
            
    def write(self,data):
        self.sock.send(data)

    def goto(self,where):
        raise GotoInterrupt(where)

    def close(self):
        self.clear()
        raise EndInterrupt

class Server:

    def __init__(self,root,host='0.0.0.0',port=5000,max_connect=5000):
        self.sock  = eventlet.listen((host,port))
        self._pool = eventlet.GreenPool(max_connect)
        self.root  = root
        self.max_connect = max_connect

    def run(self):

        root = self.root
        
        def new_connect(sock,addr):
            next_frame = root
            session = {}
            sock.send(ascii.CMD_CHAR_PER)
            flag = True
            while flag:
                try:
                    now = next_frame(self,sock,session)
                    flag = False
                except GotoInterrupt as e:
                    next_frame = e.to_where
                except EndInterrupt:
                    break
                
        s = self.sock
        try:
            eventlet.serve(s,new_connect)
        except KeyboardInterrupt:
            pass
