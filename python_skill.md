# python 奇淫技巧
*记录一些不常用，但是又很有用的python 奇淫技巧*

## 简易Web Server
```python
#python 2
python -m SimpleHTTPServer

#python 3
python -m http.server
```

## 漂亮的打印
*你可以在python repl漂亮的打印出列表和字典。*
```
  from pprint import pprint
  my_dict = {'kang':1, 'shao':2, 'shun':3}
  pprint(my_dict)
  #感觉并没有什么卵用
```

## 快速打印出json数据
**这里还是非常有用的**
```
  cat file.json|python -m json.tool
```

## 脚本性能分析
```Python
  python -m cProfile my_script.py
  #定位脚本中的性能瓶颈
```

## 列表展平
```Python
  a_list = [[1, 2], [3, 4], [5, 6]]
  print list(itertools.chain.from_iterable(a_list))
```

## for - else
*这个真是相见恨晚啊*
有个常见的构造是跑一个循环，并查找一个元素，如果这个元素找到了，我们使用break来中断这个循环，有两个场景会让循环停下来：  
  + 第一个是当一个元素被找到，break触发
  + 第二个是循环结束
现在我们也许想知道其中哪一个，才是导致循环完成的原因，for else 也就派上用场了
```
for item in container:
  if search_something(item):
    #found it
    process(item)
    break
  else:
    #didn't find anything
    not_found_in_container
```
看一个具体案例，找质数：
```
  for n in range(2, 10):
    for x in range(2, n):
      if n % x == 0:
        print str(n) + "not a prime"
        break
    else:
      print str(n) + 'is a prime'
```
