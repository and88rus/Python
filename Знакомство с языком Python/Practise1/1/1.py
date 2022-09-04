def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
    print ("Введите день недели:")
    s = input()
    if (((int(s))==1) or ((int(s))==2) or ((int(s))==3) or ((int(s))==4) or ((int(s))==5)):
     print ("это будний день")
    elif (((int(s))==6) or (int(s)==7)): 
     print ("это выходной день")

