#***
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须
#要确保文本编辑器正在使用UTF-8 without BOM编码：

#申明utf8编码 必须是第一行或第二行
#方式1
# -*- coding: utf-8 -*-


#方式2
#!/usr/bin/python  
# -*- coding: <encoding name> -*-  
#---------------------------------------------------------------
#Python注释 
#    “#” 号后的内容均为注释 -----------
#------------------------------------------


#一：基本运算
#1.0 运算符
#+  -   *   /    //(整除)   %(模，余数)   **(指数运算)
#示例
6/5     # 1.2
6//5    # 1
6 % 5  # 1
9**2    #91
9**0.5 # 3.0  开方运算


# 关系运算
# == 等于;    >;    >=;    <;    <=;    !=(不等于)
1 == 1 # True
1> 2    # False
1 != 2  # True


# 逻辑运算
# True:逻辑真     False:逻辑假
# and    or    not 
1 == 1 and 2 > 1 # True
3 > 1 and True     #True