def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(L,n):
    print (" ")
    for i in range(int(n)):
     elem = int(input((f'L[{i}] = ')))
     L.append(elem)
    



def creation_of_L1(L1,L,n):
    print (" ")
    for i in range(int(n)):
     elem = L[i]
     L1.append(elem)




def out_put_of_L(L, n):
    print (" ")
    print (str(L).strip('[]'))



def out_put_of_L1(L1, n):
    print (" ")
    print (str(L1).strip('[]'))



def cout_of_L(L, L1, n):
    k = 0
    for i in range (int(n)):
        for j in range (int(n)):
         if (L[i] == L1[j]):
           k = k + 1
           print (k)    
            

L=[]
L1 = []
n = int(input("Размер списка: "))  
creation_of_L(L, n)
out_put_of_L(L, n)
CreationOfL1(L1,L,n)
OutPutOfL1(L1, n)
CoutOfL(L, L1, n)