# linux command（补充）

## 文件及目录管理
  1.  给文件增加别名（创建符号链接/硬链接）
  ```shell
    ln cc ccAgain ：硬链接；删除一个，将仍能找到
    ln -s cc ccTo ：符号链接(软链接)；删除源，另一个无法找到
  ```
  2. 查找文件内容(使用egrep查询文件内容)
  ```
    egrep 'coding' demo.py
  ```
  3. 管道和重定向
    + 批处理命令连接执行，使用 |
    + 串联，使用分号 ;
    + 前面成功，则执行后面一条，否则不执行，用 &&
    + 前面失败，则后一条执行，使用 ||
  ```
    ls /proc && echo suss! || echo failed
  ```

## 文本处理
1. find 文件查找
```
      find . \( -name "*.txt" -o -name "*.pdf" \) -print  #查找txt 和pdf 文件
      find . -regex ".*\(\.txt|\.pdf\)$" 正则方式查找.txt和pdf
      -iregex：忽略大小写的正则
      find . ! -name "*.txt" -print #否定参数，查找所有非txt文本
      find . -maxdepth 1 - type f #指定搜索深度，打印出当前目录的文件
```

2. grep文本搜索
```
  grep match file
```
    常用参数：
    -o 只输出匹配的文本行  
    -v 只输出没有匹配的文本行
    -c 统计文本中包含文本的次数   grep -c "text" filename
    -n 打印匹配的行号
    -i 搜索时忽略大小写
    -l 只打印文件名

```
    grep "text" . -R -n    
```

3. uniq消除重复行
```
  sort unsort.txt |uniq -d  #找出重复行
```

4. cut 按列切分文本
```
  cut -f1,2 -d';' filename  #截取filename的第1,2列
```
  cut 取的单位
  + -b 以字节为单位
  + -c 以字符为单位
  + -f 以字段为单位（使用定界符）

5. **paste 按列拼接文本**

```
    cat file1
          1
          2
    cat file2
          kang
          shao
    paste file1 file2 #将file1 file2按列拼接
          1 kang
          2 shao
    默认的定界符是制表符，可以使用-d指明定界符。
    paste file1 file2 -d ";"
          1;kang
          2;shao
```

6. sed 文本替换利器
```
  sed '/^$/d' file #移除空白行
```

## 磁盘管理
  + tar解压参数说明：
    -z 解压gz文件
    -j 解压bz2文件
    -J 解压xz文件

## 进程管理工具
  ```
    ps -ajx #以完整的格式显示所有进程
    lsof -i:3306  #查看端口占用的进程状态
    lsof -u username #查看用户username的进程所打开的文件
    lsof -c init  #查看init进程当前打开的文件
    lsof -p 23295 #查看指定进程id打开的文件
  ```
  + top
    交互后，P:根据CPU使用百分比大小排序
           M:根据驻留内存大小进行排序
           i:使得top不显示闲置或者僵尸进程

## 性能监控
  + 查看CPU使用率（sar -u）
    ```
      sar -u 1 2 #后面两个参数表示监控的频率，比如例子中表示每秒采样1次，总共采样2次
      sar -q 1 2 #查看运行队列中的进程数，运行负载等

    ```
