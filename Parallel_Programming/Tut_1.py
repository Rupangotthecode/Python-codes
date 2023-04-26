import multiprocessing
import time

#sequential processing --both functions use the same process id ie the id python is running on
def square(num):
    print("square is {}".format(num*num))
    # print(os.getpid())

def cube(num):
    print("cube is {}".format(num*num*num))
    # print(os.getpid())

# time1=time.perf_counter()
# square(5)
# cube(4)
# time2=time.perf_counter()
# print(time2-time1)

# print(multiprocessing.cpu_count())
time1=time.perf_counter()
#parallel processing --both functions have different process ids as they are operating independently 
if(__name__=='__main__'):
    p1=multiprocessing.Process(target=square, args=(7,))
    p2=multiprocessing.Process(target=cube, args=(6,))
    # print(p1.is_alive())#false
    p1.start()
    p2.start()
    # print(p1.is_alive())#true
    p1.join()
    p2.join()#process is killed after termination and we cannot execute the process again in the program without declaring it again
    # print(p1.is_alive())#false

time2=time.perf_counter()
print(time2-time1)