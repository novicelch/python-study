# 这是python基础练习
# -*- coding: utf-8 -*-
__author__ = "liuchenhu";

import re, math;

print(__author__);
a = "world";
b = "liuchenhu";
c = 22;
print(a);
print("hello world");
print("hello", "world", "lch");
print("hello %s"%a);
print("hello %s"%(a,));
print("hello %s - %s"%(a, b));
print("%s is %s years ord"%(b, c));

# 数据类型
a = 22;
print("a = %s,数据类型: %s"%(a, type(a)));
a = 22.12;
print("a = %s,数据类型: %s"%(a, type(a)));
a = "awsd";
print("a = %s,数据类型: %s"%(a, type(a)));
a = 1 > 2;
print("a = %s,数据类型: %s"%(a, type(a)));
a = ['aaa', 123, 12.3];
print("a = %s,数据类型: %s"%(a, type(a)));
a = ("wasd", 34, 33.3);
print("a = %s,数据类型: %s"%(a, type(a)));
a = {"name":"liuchenhu","age":66}
print("a = %s,数据类型: %s"%(a, type(a)));
a = None;
print("a = %s,数据类型: %s"%(a, type(a)));
a = True and False;
print("a = %s,数据类型: %s"%(a, type(a)));
a = set(["wasd", True, None, 212, 22.3]);
print("a = %s,数据类型: %s"%(a, type(a)));

# 运算符
print(123//2);
print(23%2);
print(3**2);

# 字符串
print(u"刘陈虎");
print(r"刘白");
print(b"liubai");

# ASCII码
print("98-->%s;a-->%s"%(chr(98),ord('a')));
print("刘陈虎".encode("utf8"));
print(b'\xe5\x88\x98\xe9\x99\x88\xe8\x99\x8e'.decode("utf-8"));

