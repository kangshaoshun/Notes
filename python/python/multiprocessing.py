#coding:utf-8
import sys
from multiprocessing import Queue, Process
reload(sys)
sys.setdefaultencoding('utf-8')

def write(q):
    print q.get(True)

def read(q):
    print q.get(True)

if __name__ == '__main__':
    q = Queue()
    help(q)
    d = {'kang': "shao", "shao":"shun"}
    q.put(d)
    q.put(d)
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    pr.terminate()




