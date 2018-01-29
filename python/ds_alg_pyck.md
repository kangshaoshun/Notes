# python cookbook读书笔记

## 1.数据结构与算法
#### 保留最后N个元素

```
from collections import deque
q = deque(maxlen=3)	#创建双端队列容器,该队列保存最后出现在队列中的n个元素
q.append(1)
q.append(2)
q.append(3)
q.append(5)
print q		#deque([2, 3, 5], maxlen=3)

q.appendleft(6)	#在队列首端添加元素，当然队列长度依然是3
q.popleft()	#弹出队列首端元素
```
ps:deque在队列首端弹出和插入操作的时间复杂度都是O(1),而普通list都是O(N)

这个deque应用场景还是蛮多的


