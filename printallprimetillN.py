import math
low=int(input())  
high=int(input())  
  
for Num in range(low,high+1):  
   if Num==1:
       print(Num)
   if num > 1:
        for i in range(2,int(math.sqrt(Num)+1)):  
            if (Num % i)==0:  
                break  
        else:  
            print(Num) 
            
