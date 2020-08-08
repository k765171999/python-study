# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:14:46 2020

@author: LvGJ
"""
#%% =====================================================================

f = open("testRead.txt",'r')
with open('testRead.txt', 'r') as f2:
    print(f2.read())
    
#%% ===================== String IO& BytesIO ============================

from io import StringIO

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    
from io import BytesIO

#%% ====================== 操作文件和目录 ==============================

import os

print(os.name)
print(os.environ)
print('================')
print(os.environ.get('PATH'))
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('C:/Users/LvGJ/Documents/PostGraduate/Program/python/Advanced Features', 'testdir')
os.mkdir('C:/Users/LvGJ/Documents/PostGraduate/Program/python/Advanced Features/testdir')
os.rmdir('C:/Users/LvGJ/Documents/PostGraduate/Program/python/Advanced Features/testdir')

#%% ============================== 序列化 ==================================
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

#写如文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 重新读回来
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d


#%% ==== 进程 ===
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)



#%% =====
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)







    
    