def toplama(a,b):
    return a+b

def carpma(a,b):
    return a*b

def bolme(a,b):
    if(b>0):
        return a/b
    else:
        print("Payda kısmına 0 gelemez!!!")
        return False

x=int(input("Lütfen ilk sayıyı giriniz:"))
y=int(input("Lütfen ikinci sayıyı giriniz:"))
print(toplama(x,y))
print(carpma(x,y))