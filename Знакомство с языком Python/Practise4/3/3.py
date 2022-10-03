def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(L, n):
    print (" ")
    for i in range(int(n)):
     elem = int(input((f'L[{i}] = ')))
     L.append(elem)
    



def out_put_of_L(L, n):
    print (" ")
    print (str(L).strip('[]'))




def cout_of_L(L, L1, n):
    for i in range (int(n)):
        if (L.count(L[i]) == 1):
            L1.append(L[i])




def out_put_of_L1(L1, n):
    print (" ")
    print (str(L1).strip('[]'))



L = []
L1 = []
n = int(input("Размер списка: "))  
creation_of_L(L, n)
out_put_of_L(L, n)
cout_of_L(L, L1, n)
out_put_of_L1(L1, n)
