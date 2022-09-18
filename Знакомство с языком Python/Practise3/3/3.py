from decimal import Decimal
import math
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
def CreationOfMassive(s, L):
   print (" ")
   for i in range(int(s)):
     elem=float(input((f'L[{i}] = ')))
     L.append(elem)
def OutPutOfMassive(s,L):
    print (" ")
    print (str(L).strip('[]'))
L=[]
s=int(input("Размер списка: "))
CreationOfMassive(s,L)
OutPutOfMassive (s,L)  
d=2.005
a=str(d)
x = Decimal(str(d))
y = int(float(str(d)))
z=x-y
print (x)
print (y)
print (z)