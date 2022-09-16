from array import*
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
def SumOfSymb(a):
    c=a
    size =2
    while ((a>=10)):
        a=a//10
        size=size+1
    m = array('i', (0 for i in range(0, size)))
    for i in range(size-1,0,-1):
        m[i] = c%10
        c=c//10
    sum=0
    for i in range (0,size,1):
        sum=sum+m[i]
    return sum
n=float(input("n = "))
while (float.is_integer(n)==False):
     n*=10
print ("Сумма цифр числа n - ", SumOfSymb(int(n)))

