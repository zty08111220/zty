import time
#引入time模块
start=time.time()
#start=time.perf_counter()这种更为精确
#需要测量时间的程序代码 省略
end=time.time()
#end=time.perf_counter()这种更为精确
print("程序执行时间:",end-start,"秒")