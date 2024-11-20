# 题目：时间记录装饰器
# 描述： 编写一个装饰器 time_decorator，它能够记录并打印被装饰函数的执行时间。
# 具体要求如下：
# 1. 基本功能：装饰器应该能够记录被装饰函数的名称及其执行时间，并将这些信息输出到控制台。
# 2. 不带参数的装饰器：不需要支持带参数的装饰器功能。

import datetime
import time


def time_decorator(func):
    def acc(*args,**kwargs):
        time1=datetime.datetime.now()
        result=func(*args,**kwargs)
        time2=datetime.datetime.now()
        print(f'该方法用时为：{time2-time1}')
        return result

    return acc

@time_decorator
def add():
    a=5
    b=7
    time.sleep(3)
    print(a+b)
add()


# import logging
# from functools import wraps
#
# # 配置日志
# logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
#
#
# def log_decorator(level="INFO"):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             # 获取日志级别
#             log_level = getattr(logging, level.upper(), logging.INFO)
#
#             # 记录函数调用信息
#             logging.log(log_level, f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
#
#             # 调用函数并获取返回值
#             result = func(*args, **kwargs)
#
#             # 记录函数返回信息
#             logging.log(log_level, f"{func.__name__} returned {result}")
#
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # 示例1：带参数的装饰器
# @log_decorator(level="DEBUG")
# def add(a, b):
#     return a + b
#
#
# # 示例2：不带参数的装饰器
# @log_decorator
# def multiply(a, b):
#     return a * b
#
#
# # 测试
# if __name__ == "__main__":
#     result_add = add(3, 5)
#     result_multiply = multiply(4, 6)

def timing(status='Train'):
    def dec(func):
        # @functools.wraps(func)
        # def wrapper(*args, **kwargs):
        #     start = time.time()
        #     func1 = func(*args, **kwargs)  # 此处做了一个变形
        #     print('[%s] time: %.3f s ' % (status, time.time() - start))
        #     return func1
        start = time.time()
        func1 = func()  # 此处做了一个变形
        print('[%s] time: %.3f s ' % (status, time.time() - start))



    return dec


@timing(status='Train')
def Training():
    time.sleep(3)

#Training=timing(status='Train')(Training)
#Training=timing(status='Train')(Training)


