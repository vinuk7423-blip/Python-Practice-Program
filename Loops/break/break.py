n=int(input("enter a number:"))
for i in range(2,n+1):
    if n % i == 0:
        break
if i == n:
    print("prime number")
else:
    print("not prime number")