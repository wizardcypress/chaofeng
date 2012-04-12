from chaofeng.ascii import *

def load_static():
    from os import walk as os_walk
    '''Load the file under static path as string.'''
    path='./static/'
    v = {}
    for root,dirs,files in os_walk(path):
        for filename in files :
            f = open(path+filename,'r')
            v[filename] = move2(0,0)+clear+f.read()[0:-1]
    return v

static = load_static()
