#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
This module is core of chaofeng. It implements the Session,Frame,Server.

The Server will listen to the port for a request. And then, A Session
object will be instanced, and will be send into the root frame.
'''

__version__ = '0.04'

from asyncore import dispatcher
from asynchat import async_chat
from chaofeng.ascii import *
from os import walk as os_walk
import socket, asyncore

class MultiInputError(Exception):pass

class Session(async_chat,dict):
    '''The session object is used to record a session to user.'''
    
    def __init__(self,server,sock):
        async_chat.__init__(self,sock)
        self.set_terminator(None)
        self.server = server
        # Force send char like 'getch'
        self.push(CMD_CHAR_PER)

    def collect_incoming_data(self, data):
        self.frame.get(data)

    def goto(self,frame):
        ''' From a frame to an other frame. '''
        try: cur = self.frame
        except AttributeError: pass
        else: cur.clear()
        self.frame = frame(self)
    
    def found_terminator(self):
        pass
    
    def handle_close(self):
        if self.hasattr('frame') : self.frame.clear()
        async_chat.handle_close(self)
        self.server.sessions.remove(self)

    def nothing(self):
        pass

class Frame:
    ''' A base object to the frame. '''
    def __init__(self,session):
        self.session = session
        self.initialize()

    def initialize(self):
        '''Hook for subclass initialization.'''
        pass
    
    def clear(self):
        '''Hook for leave this frame.'''
        pass

    def get(self,data):
        '''Hook for subclass when keydown.'''

    def write(self,data):
        '''Write info to the session.'''
        self.session.push(data)

    def goto(self,frame):
        self.session.goto(frame)

    def close(self):
        self.session.handle_close()

    def nothing(self,*argu1,**argu2):
        pass
        
class Server(dispatcher):
    ''' The object will accept the request and handle it.'''
    
    def __init__(self,root,host='',port=5000):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.sessions = []
        self.static = {}
        self.root = root

    def handle_accept(self):
        conn, addr = self.accept()
        new = Session(self, conn)
        new.goto(self.root)
        self.sessions.append(new)
        
    def load_static(self,path='./static/'):
        '''Load the file under static path as string.'''
        for root,dirs,files in os_walk(path):
            for filename in files :
                f = open(path+filename,'r')
                self.static[filename] = move2(0,0)+clear+f.read()[0:-1]
            
    def run(self):
        self.load_static()
        asyncore.loop()
