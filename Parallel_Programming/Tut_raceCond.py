import multiprocessing

def withdraw(balance):
    for i in range(10):
        balance.value-=1
       

def deposit(balance):
    for i in range(10):
        balance.value+=1
        


def perform_transactions():
    balance = multiprocessing.Value('i',100) 
    #created a critical section consisting of the object {value:100}

    p1=multiprocessing.Process(target=withdraw,args=(balance,))
    p2=multiprocessing.Process(target=deposit,args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"final balance={balance.value}")

if __name__ == '__main__':
    for i in range(10):
        perform_transactions()
# We needed 100 to be the final result but we received 108
# This happened due to both processes trying to use the common critical section simultaenously 

