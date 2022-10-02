from decimal import Decimal
import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def CreationOfListL1(s, L1):
   print (" ")
   for i in range(int(s)):
     elem = float(input((f'L[{i}] = ')))
     L1.append(elem)




def OutPutOfListL1(s, L1):
    print (" ")
    print (str(L1).strip('[]'))




def CreationOfListL2(s, L1, L2):
    for i in range (int(s)):
        elem = float(Decimal(str(L1[i])) - int(float(str(L1[i]))))
        L2.append(elem)




def MinOfL2(s, L2):
    min = L2[0]
    for i in range (int(s)):
     if ((L2[i] < min) & (L2[i] != 0.0)):
        min = L2[i]
    return (min)




def MaxOfL2(s, L2):
    max = L2[0]
    for i in range (int(s)):
     if (L2[i] > max):
        max = L2[i]
    return (max)




L1 = []
L2 = []
s = int(input("Размер списка: "))
CreationOfListL1(s, L1)
OutPutOfListL1 (s, L1) 
CreationOfListL2(s, L1, L2)
print (" ")
print (abs(MaxOfL2(s, L2) - MinOfL2(s, L2)))