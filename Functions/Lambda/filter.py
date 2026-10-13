lst=[10,20,35,40]
def num (x):
    if x % 2 == 0:
        return True
    else:
        return False
evn_lst=list(filter(num,lst))
print(evn_lst)


