
2016.3.21
---------


我去我终于把曹一的[第二次作业程序][1]看懂了。

程序第110~113行是：
```
if (Asc_Table[(ord(str[k])-32)*5+j] >> (i) & 1): 
    b.append('#') 
else: 
    b.append(' ') 
```
而 ``Asc_Table`` 长这样：
```
Asc_Table=[0x00, 0x00, 0x00, 0x00, 0x00, # ' ' 
         0x00, 0x00, 0x5F, 0x00, 0x00,   #  ! 
         0x00, 0x07, 0x00, 0x07, 0x00,   #  " 
         ...
```
其中的 ``>>`` 是shifting operation:
> These operators accept plain or long integers as arguments. The arguments are converted to a common type. They shift the first argument to the left or right by the number of bits given by the second argument.

>A right shift by n bits is defined as division by pow(2, n). A left shift by n bits is defined as multiplication with pow(2, n). Negative shift counts raise a ValueError exception.[^shifting-operations]

``a >> b`` 就是把整数a换为二进制数，然后向右移动b位。``a << b`` 则是向左。

而 ``&`` 是binary bitwise operation。``x & 1`` 等价于  ``x % 2 == 1``。我不想写了具体可以看[python docs][2]或者[wikipedia][3]。。。

-----------

总之，这一段代码的作用是将整数 ``Asc_Table[(ord(str[k])-32)*5+j]`` 转换为二进制数后，按照每一位是 0 还是 1 向 ``b`` 中加入空格或者井号，成为图像的一列( 7×1 )。 ``Asc_Table`` 的每 5 个数表示一个 7×5 的图像，对应一个字符，也就是说 ``Asc_Table`` 中的数储存了字符的图像信息。


好的，以上懂了的话，那我们做一个简单的练习：
```
j = [0x20, 0x40, 0x44, 0x3D, 0x00]

for row in range(7):
	for col in range(5):
		if j[col] >> row & 1: # or write "if (j[col] >> row) % 2 == 1:" instead
			print '#',
		else:
			print ' ',
	print 
```
试着运行一下这段代码，你看到了什么？能解释原因吗？



[^shifting-operations]:https://docs.python.org/2/reference/expressions.html#shifting-operations

[1]:https://github.com/breakingDboy/computational_physics_2013301020120/blob/master/show_gif.py
[2]:https://docs.python.org/2/reference/expressions.html#binary-bitwise-operations
[3]:https://en.wikipedia.org/wiki/Bitwise_operation
