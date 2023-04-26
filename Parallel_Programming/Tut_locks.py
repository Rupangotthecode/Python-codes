import multiprocessing

# Here we will solve the race consition using locks

def withdraw(balance,lock):
    lock.acquire()
    for i in range(10):
        balance.value-=1
    lock.release()
       

def deposit(balance,lock):
    lock.acquire()
    for i in range(10):
        balance.value+=1
    lock.release()
        


def perform_transactions():
    balance = multiprocessing.Value('i',100) 
    #created a critical section consisting of the object {value:100}

    lock=multiprocessing.Lock()
    # Here we have created a lock which allows only one process at a time to access critical section

    p1=multiprocessing.Process(target=withdraw,args=(balance,lock))
    p2=multiprocessing.Process(target=deposit,args=(balance,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"final balance={balance.value}")

if __name__ == '__main__':
    for i in range(10):
        perform_transactions()