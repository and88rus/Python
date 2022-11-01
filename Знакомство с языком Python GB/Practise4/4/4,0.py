import random




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def List(L,k,i): 
   a=0
   b=0
   unL=[]
   if (i==0):
    b = k
    a = random.randint(0,100)
   else:
    a = random.randint(0,100)
    b = random.randint(0,k)
   unL.append (a)
   unL.append (b)
   print (unL)
   L.append(unL)





def sum_of_L(L,L1,M,L2):
  for i in range (0,len(L)):
    if L[i][1] in M:
      continue
    c=L[i][0]
    d=L[i][1]
    print (i,c)
    for j in range (i+1,len(L)):
        if ((L[i][1]==L[j][1])):
            c+=L[j][0]
            M.append(L[j][1])
            print (i,j,c) 
    L1.append(c)
    L2.append(d)



def Itog(L3, a, b,L4):
    unL=[]
    for i in range (0, 1):
       unL.append (a)
       unL.append (b)
    L4.append(unL)





def voz(L4):
  if ((L4[i][0]==0) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==0) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]>1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]>1) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==0) and (L4[i][1])>1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])>1):
     return "^"
  elif ((L4[i][0]>1) and (L4[i][1])>1):
     return "^"
  
  
 

  

def deg(L4):
  if ((L4[i][0]==0) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==0)and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==1)and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]>1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]>1)and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==0) and (L4[i][1])>1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])>1):
     return str(L4[i][1])
  elif ((L4[i][0]>1) and (L4[i][1])>1):
     return str(L4[i][1])
 
  

  
def x(L4):
  if ((L4[i][0]==0) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==0) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==1):
     return "x"
  elif ((L4[i][0]>1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]>1)and (L4[i][1])==1):
     return "x"
  elif ((L4[i][0]==0) and (L4[i][1])>1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])>1):
     return "x"
  elif ((L4[i][0]>1) and (L4[i][1])>1):
     return "x"
 


 
def c(L4):
  if ((L4[i][0]==0) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==0) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==0):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])==1):
     return ""
  elif ((L4[i][0]>1) and (L4[i][1])==0):
     return str(L4[i][0])
  elif ((L4[i][0]>1)and (L4[i][1])==1):
     return str(L4[i][0])
  elif ((L4[i][0]==0) and (L4[i][1])>1):
     return ""
  elif ((L4[i][0]==1) and (L4[i][1])>1):
     return ""
  elif ((L4[i][0]>1) and (L4[i][1])>1):
     return str(L4[i][0])



def sort_of_L4_up(L4): 
    t=0
    for j in range(0,len(L4)-1):
        for i in range(0,len(L4)-j-1):
            if (L4[i][1] < L4[i+1][1]):
                t=L4[i]
                L4[i]=L4[i+1]
                L4[i+1]=t




def plus(i,L4):
    if (i!=len(L4)-1):
        return (" + ")
    else: 
        return ('')




L=[]



L1=[]


L2=[]



L3=[]



L4=[]




M=[]




k = int(input("k = "))



for i in range (0, int(k)+1):
 List(L,k,i)



print ("")


print (L)


print ("")

print ("")

sum_of_L(L,L1,M,L2)

print ("")

print (L)

print ("")

print (L1)

print ("")

print (L2)

print ("")


for i in range (0, len(L2)):
    Itog(L3,L1[i],L2[i],L4)


sort_of_L4_up(L4)

for i in range (0, len(L4)):
    L4[i][0]=random.randint(0,100)

print (L4)

print ("")


for i in range (0,len(L4)):
    print (f'{c(L4)}{x(L4)}{voz(L4)}{deg(L4)}{plus(i,L4)}',end = " ")
    if (i==len(L4)-1):
         print ("= 0")
print()




data = open('for 4 of 4.txt','w')

for i in range (0,len(L4)):
  data.write(c(L4))
  data.write(x(L4))
  data.write(voz(L4))
  data.write(deg(L4))
  data.write(plus(i,L4))
  if (i==len(L4)-1):
         data.write (" = 0")

data.close()

exit()



