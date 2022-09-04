def print_hi(name):
    print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')
    from array import *
    s = input()
    m = array('i', (0 for i in range(0, int(s))))
    for i in range(int(s)): m[i] = int(input())
    print(m)
    for i in range(int(s)-1):
      for j in range(int(s)-1):
          if (m[j]>=m[j+1]):
              m[j],m[j+1]=m[j+1],m[j]
print(m)