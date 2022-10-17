import random




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(L,n):
    for i in range(int(n)):
        elem=random.random()*random.randint(a,b)
        L.append(elem)




def output_of_L(L):
    print (L)




L=[]



n = int(input("n = "))
print (" ")


a = int(input("a = "))
print (" ")


b = int(input("b = "))
print (" ")



creation_of_L(L,n)



output_of_L (L)