#!/usr/bin/python  
#coding:utf-8  

""" 
@author: Ele 
@contact: xx@xx.com 
@software: PyCharm 
@file: testList.py 
@time: 2018/11/10 11:45 
"""


def main():
    var_args('yasoob', 'python', 'eggs', 'test')
    arg =('yasoob', 'python', 'eggs', 'test')
    var_args(*arg)

    greet_me(name="yasoob")
    a = {'name':"yasoob"}
    greet_me(**a)

    args_kwargs(3,"two",5)
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    args_kwargs(**kwargs)
    args = (3, "two", 5)
    args_kwargs(*args)
    pass


def var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
    print(argv)
    print(*argv)


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
    print(kwargs)



def args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


if __name__ == "__main__":
    main()