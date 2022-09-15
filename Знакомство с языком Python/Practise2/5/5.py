from array import*
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
def SumOfSymb(a):
    c=a
    size =1 
    while ((a>=10)):
        a=a/10
        size=size+1
    m = array('i', (0 for i in range(0, size)))
    for i in range(size-1,0,1): 
        m[i] = c%19
        c=c/10
    sum=0
    