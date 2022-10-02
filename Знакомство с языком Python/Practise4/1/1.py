import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




    def Pi(d):
        k = 0
        while ((float.is_integer(d)) == False):
         d *= 10
         k = k + 1
        return(round(math.pi, k))




    d = float(input("d = "))
    print (" ")
    if (0.00000000001 <= d <= 0.1):
     print (f'Pi = {Pi(d)} c точностью d = {d}')
    else: 
     print ("d > 0.1 or d < 0.00000000001")
