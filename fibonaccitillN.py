
n= int(input())
n1, n2 = 0, 1
count = 0
print("Fibonacci series:")
if n == 1:
   print(n)
   print(n1)
else:
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       Print(COUNT)
