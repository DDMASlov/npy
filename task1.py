filename = input("enter filename:")
x = float(input("enter x:"))
number = []
p = 0.0
der = 0.0
try:
    with open(filename,'r') as f:
        text = f.read()
        words = text.split()
    for b in words:
        try:
            number.append(float(b))
        except ValueError:
            print("bad value")
    n = 1
    p = p + number[0]
    for i in range(1,len(number)):
        der = der+(i)*number[i]*n
        n = n*x
        p = p+number[i]*n
    print("polynomial:",p)
    print("derivative:",der)
except FileNotFoundError:
    print("can't open the file!")