import eventlet
from chaofeng import ascii

class GotoInterrupt(Exception):
    
    def __init__(self,to_where):
        self.next = to_where

class EndInterrupt(Exception): pass

class Frame:

    buffer_size = 1024
    
    g = {}

    def __init__(self,server,sock,session):
        self.session = session
        self.server = server
        self.sock = sock
        self.initialize()

    def loop(self):
        while True:
            data = self.read()
            self.get(data)

    def initialize(self):
        pass

    def clear(self):
        pass

    def get(self,data):
        pass

    def read(self,buffer_size=1024):
        data = self.sock.recv(buffer_size)
        if not data :
            self.clear()
            raise EndInterrupt
        else:
            return data
            
    def write(self,data):
        self.sock.send(data)

    def goto(self,where):
        raise GotoInterrupt(where)

    def close(self):
        raise EndInterrupt

class Server:

    def __init__(self,root,host='0.0.0.0',port=5000,max_connect=5000):
        self.sock  = eventlet.listen((host,port))
        self._pool = eventlet.GreenPool(max_connect)
        self.root  = root
        self.max_connect = max_connect

    def run(self):
        
        def new_connect(sock):
            next_frame = self.root
            session = {}
            sock.send(ascii.CMD_CHAR_PER)
            while True:
                try:
                    now = next_frame(self,sock,session)
                    now.loop()
                except GotoInterrupt,e:
                    new_frame = e.to_where
                except EndInterrupt:
                    break
                
        s = self.sock
        while True:
            new_sock, address = s.accept()
            self._pool.spawn_n(new_connect,new_sock)
