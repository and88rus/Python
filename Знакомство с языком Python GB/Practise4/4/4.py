def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




data = open('file.txt','w+')
data.writelines ("Hello")
data.close