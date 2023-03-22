import time
start_time = time.time()
list_ = [i for i in range(1,100000000)]
finish_time = time.time()
result =finish_time - start_time
print(list_)
print (result)