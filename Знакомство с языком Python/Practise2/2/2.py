def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
    s = input("N=")
    p=[]
    m=[i+1 for i in range (int(s))]
    sum=1
    for i in range(int(s)):
        sum*=m[i]
        p.append(sum)
    print(p)