def print_hi():
    print()
if __name__ == '__main__':
    print_hi()
    from math import sqrt
    def DistanceBetween2Points(x1,x2,y1,y2):
        d=sqrt((x2-x1)**2+((y2-y1)**2))
        return d
    print ("Введите координаты точки A")
    x1 = input("x=")
    y1 = input("y=")
    print ("Введите координаты точки B")
    x2 = input("x=")
    y2 = input("y=")
    print (DistanceBetween2Points(x1,y1,x2,y2))