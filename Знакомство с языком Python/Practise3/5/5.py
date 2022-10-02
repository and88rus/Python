import math
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
def Fibonacci(n):
    if (n>=2):
        return Fibonacci(n-1)+Fibonacci(n-2)
    elif (n==1):
        return 1
    elif (n==0):
        return 0
    elif (n<0):
        return int(math.pow(-1,(-1*n+1))*Fibonacci(-1*n))
def CreatingOfFibonacciArray(n,L):
    for i in range (-int(n),int(n)+1,+1):
     elem=Fibonacci(i)
     L.append(elem)
def OutPutOfL(L):
   print (" ")
   print (str(L).strip('[]')) 
L=[]
n=int(input("k = "))
CreatingOfFibonacciArray(n,L)
OutPutOfL(L)
