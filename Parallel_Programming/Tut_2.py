import multiprocessing

#data management problem among processes

result=[]
def list_sq(myList):
    for i in myList:
        result.append(i*i)
    print("result={}".format(result))
mylist=[1,2,3,4]
if(__name__=='__main__'):
    p1=multiprocessing.Process(target=list_sq,args=(mylist, ))
    p1.start()
    p1.join()

#here the code prints [1,4,9,16] whereas if we print result normally it will return null array
#this is because the main branch does not know that the process we have made has caused a change in the result variable
print(result)
#notice how result in the print statement will be printed twice. This is because the first print is occuring when the normal execution 
#occurs and the next one when the p1 process merges with the sequence