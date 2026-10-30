text=input("Enter a string:")
vowels=0
constants=0
digits=0
spaces=0
for ch in text:
    if ch.isalpha():
        if ch.lower()in"aeiou":
            vowels+=1
        else:
            constants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces +=1
        print("Vowels:",vowels)
        print("Constants:",constants)
        print("Digits:",digits)
        print("Spaces:",spaces)    