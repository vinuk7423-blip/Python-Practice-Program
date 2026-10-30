text=input("Enter a string:")
frequency={}
for ch in text:
    if ch!="":
        frequency[ch]=frequency.get(ch,0)+1
        print("Character Frequency:",frequency)