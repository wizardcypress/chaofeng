cháofēng
========

Cháofēng is a simple telnet bbs framework for python.

Hello, world
------------

Here is a simple example app for Chaofeng :

```python
from bbs import Frame, Server
import ascii as c

class Hello(Frame):

    def initialize(self):
        self.write('Hello,World!')

    def clear(self):
        self.write('Don leave me alone ...\n')

if __name__ == '__main__' :
    s = Server(Hello)
    s.run()
```

作为服务器，你可以这样运行：

```bash
python /path-to-the-file/
```

作为客户端，你可以这样(在linux)：

```bash
telnet host port
```

一般的，本地的host是填loaclhost，port是5000。所以如果服务器是本地的话，你可以：

```bash
telnet localhost 5000
```
