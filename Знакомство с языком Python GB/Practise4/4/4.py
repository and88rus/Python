def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



x= f'{int(2)}{"x"}{""}{""}'+f'{int(2)}{"x"}{""}{""}'
data = open("file.txt","w")
data.writelines (x)
data.close