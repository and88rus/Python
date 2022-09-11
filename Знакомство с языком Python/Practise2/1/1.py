def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
    from array import *
    s = input("N=")
    p=[]
    m = array('i', (0 for i in range(0, int(s))))
    for i in range(int(s)): m[i] = i+1
    sum=1
    for i in range(int(s)):
        sum*=m[i]
        p.append(sum)
    print(p)
