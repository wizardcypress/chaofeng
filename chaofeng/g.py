from chaofeng.ascii import *

STATIC_PATH = './static'

def load_static():
    from os import walk as os_walk
    '''Load the file under static path as string.'''
    path=STATIC_PATH
    v = {}
    for root,dirs,files in os_walk(path):
        for filename in files :
            f = open(path+filename,'r')
            v[filename] = move2(0,0)+clear+f.read()[0:-1]
    return v

static = load_static()

marks = {}

def mark(name):
    def mark_inner(frame):
        global marks
        mraks[name] = frame
        return frame
    return mark_inner
