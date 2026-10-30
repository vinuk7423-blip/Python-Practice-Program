number=[12,15,20,23,30,35,40]
even=[]=odd=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
        print("Even Numbers:",even)
        print("Odd numbers:",odd)    