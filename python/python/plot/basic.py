#coding:utf-8
import sys
import matplotlib.pylab as plt
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

#画布
plt.figure(figsize=(10,6), dpi=80, num=1)
"""
figure可接受参数：
   参数     默认值      描述
   num      1        图像的数量
   figsize          图像的长和宽
   dpi               分辨率
   facecolor         绘图区域的背景颜色
   edgecolor        绘图区域边缘的颜色
   frameon          是否绘制图像的边缘
"""

plt.subplot(1, 1, 1)

#制造数据
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

#画图
plt.plot(X, C, color="blue", linewidth=3.0, linestyle='-')
plt.plot(X, S, color="red", linewidth=3.0, linestyle='-')

#横纵坐标打上坐标轴
plt.xlim(-4.0, 4.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.ylim(-1.0, 1.0)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

"""
#(横纵坐标打上坐标轴的标准做法)
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
plt.xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, xmax + dy
"""

#显示
plt.show()
