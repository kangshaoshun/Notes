## AWK NOTES

### awk模式
1. **BEGIN {语句}**
	+ 在读取任何输入前执行一次 语句
2. **END{语句}**
	+ 读取所有输入之后执行一次 语句
3. **表达式{语句}**
	+  对于表达式为真（即非零或非空）的行，执行 语句
4. **/正则表达式/{语句}**
	+ 如果输入行包含字符串与 正则表达式 相匹配，则执行 语句
5. **组合模式{语句}**
	+ 一个组合模式通过与(&&),或(||),非（|），以及括弧来组合多个表达式，对于组合模式为真的每个输入行，执行 语句
6. **模式1，模式2{语句}**
	+ 范围模式(range pattern)匹配从 与模式1相匹配的行到与模式2相匹配的行（包括该行）之间的所有行，对于这些输入行，执行语句

### 常用命令(陌生的)
*操作数据：*

	Beth	4.00	0
	Dan	3.75	0
	kathy	4.00	10
	Mark	5.00	20
	Mary	5.50	22
	Susie	4.25	18

+ 高级输出

	``` {printf("total pay for %s is $%.2f\n", $1, $2*$3)}```

+ 选择

	```$2 * $3 > 50 { printf("$%.2f for %s\n", $2 * $3, $1) }```

+ 数据验证

	```
	NF != 3     { print $0, "number of fields is not equal to 3" }
	```
+ 计数
	```
		$3 > 15 { emp = emp + 1 } END     { print emp, "employees worked more than 15 hours" }
	```

+ 求平均值
	```
	    { pay = pay + $2 * $3 }END { print NR, "employees"  print "total pay is", pay print "average pay is", pay/NR  }
	```

+ 处理文本
```
	$2 > maxrate { maxrate = $2; maxemp = $1 }
END { print "highest hourly rate:", maxrate, "for", maxemp }
```

+ 字符串连接

	```
	    { names = names $1 " "}	END { print names }
	```

+ 内置函数

	```
	{ print $1, length($1) }
	```

+ for语句

	```
	{ for (i = 1; i <= $3; i = i + 1)
    	printf("\t%.2f\n", $1 * (1 + $2) ^ i)
	}
	```

+ 数组

	```
		    { line[NR] = $0 }  
				END { i = NR  
      		while (i > 0) {
        	print line[i]
        i = i - 1
      }
    }
	```
