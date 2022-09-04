def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
    x = input("x=")
    y = input("y=")
    if (((int(x))>0 and ((int(y))>0))):
     print ("I")
    elif (((int(x))<0 and ((int(y))>0))): 
     print ("II")
    elif (((int(x))<0 and ((int(y))<0))): 
     print ("III")
    elif (((int(x))>0 and ((int(y))<0))): 
     print ("IV")
    elif (((int(x))==0 and ((int(y))==0))): 
     print ("четверть неопределена")