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
## 网络工具
  + 查询网络服务和端口
    *netstat命令用于显示各种网络相关信息，如网络连接，路由表，接口状态，masquerade连接，多播成员等*
    + 列出所有端口
    ```
      netstat -a
    ```
    + 列出所有tcp端口
    ```
      netstat -at
    ```
    + 列出所有有监听的服务状态
    ```
      netstat -l
    ```
  + 网络路由
    + 查看路由状态
    ```
      route -n
    ```
    + 发送ping包到地址IP
    ```
      ping IP
    ```
    + 探测前往地址IP的路由路径
    ```
      traceroute IP
    ```
    + DNS查询，寻找域名domain对应的IP
    ```
      host domain
    ```
    + 反向DNS查询
    ```
      host IP
    ```
    + ftp sftp lftp ssh
    ```
      sftp ID@host    #登录服务器host
    ```
    sftp登陆服务器之后，可以用下面的命令一步操作：
      + get filename  下载文件
      + put filename  上传文件
    + lftp同步文件夹（类似rsync工具）
    ```
      lftp -u user:pass host
      lftp user@host:~>mirror -n
    ```
  + 网络复制
      + 将本地localpath指向的文件上传到远程主机的path路径
      ```
        scp localpath ID@host:path
      ```
      + 以ssh 协议，遍历下载path路径下的整个文件系统，到本地的localpath
      ```
        scp -r ID@site:path localpath
      ```
## 用户管理
  1. 用户
    + 添加用户
      ```
        useradd -m username
        passwd username
      ```
    + 删除用户
      ```
        userdel -r username
      ```
  2. 用户的组
    + 将用户添加到组
      ```
        groups
        usermod -G groupName username //将用户添加到组
        usermod -g groupName username  //变更用户所属的根组（将用户加入到新组，并从旧组中删除）
      ```
    + 查看系统所有组
      ```
        more /etc/passwd
        more /etc/group
      ```
  3. 环境变量
      + bashrc与profile都用于保存用户的环境信息，bashrc用于交互式non-loginshell，而profile用于交互式login shell
      + /etc/profile，/etc/bashrc 是系统全局环境变量设定  ~/.profile，~/.bashrc用户目录下的私有环境变量设定
      + 1.首先读入的是全局环境变量设置文件/etc/profile，然后根据其内容读取额外的文档，如/etc/profile.d和/etc/inputrc
        2.读取当前登录用户Home目录下的文件~/.bash_profile，其次读取~/.bash_login最后读取~/.profile，这三个文档设定基本上是一样的，读取有优先关系
        3.读取~/.bashrc
      + ~/.profile与~/.bashrc的区别:
        这两者都具有个性化定制功能
          ~/.profile可以设定本用户专有的路径，环境变量，等，它只能登入的时候执行一次
          ~/.bashrc也是某用户专有设定文档，可以设定路径，命令别名，每次shell script的执行都会使用它一次

## 系统管理
  1. 查询系统版本
    ```
      uname -a
      lsb_release -a
      more /etc/release
    ```
  2. 查询硬件信息
    ```
      sar -u 5 10
      cat /proc/cpuinfo  //查询CPU信息
      cat /proc/cpuinfo | grep processor | wc -l  //查询CPU个数
      arch 显示架构
    ```
