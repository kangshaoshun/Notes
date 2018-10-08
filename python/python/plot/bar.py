#coding:utf-8
import sys

import matplotlib.pyplot as plt
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

labels = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']

data = [5, 20, 15, 25, 10]
#plt.bar(range(len(data)), data)
#bar函数的函数签名  bar(left, height, width=0.8, bottom=None, **kwargs)

#设置横坐标
#plt.bar(range(len(data)), data, tick_label= labels)



#显示一个并列的柱状图（这个在实际生活当中很常用），可以作为一个demo
size = 5
x = np.arange(size)
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + width * 2, c, width=width, label='c')
plt.legend()
plt.show()

