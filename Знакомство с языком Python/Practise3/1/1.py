def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def CreationOfMassive(s, L):
   print (" ")
   for i in range(int(s)):
     elem = int(input((f'L[{i}] = ')))
     L.append(elem)




def OutPutOfMassive(s, L):
    print (" ")
    print (str(L).strip('[]'))




def SumOfElem(s, L):
    sum = 0
    for i in range(int(s)): 
          if (i % 2 == 1):
            sum += L[i]
    print (" ")
    print ("Сумма элементов на нечетных позициях:")
    print (" ")
    print (sum)




L = []
s = int(input("Размер списка: "))
CreationOfMassive(s, L)
OutPutOfMassive (s, L)
SumOfElem(s, L)