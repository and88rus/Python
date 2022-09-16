import random
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
def RandomElemInLem(s):
    L=[]
    print (" ")
    for i in range(int(s)): 
      elem=int(input(("L[i] = ")))
      L.append(elem)
    print (" ")
    print (L)
    print (" ")
    random.shuffle (L)
    print (L)
    print (" ")
s=int(input("Размер списка: "))
print (" ")
RandomElemInLem(s)