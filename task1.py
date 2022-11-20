filename = input("enter filename:")
x = float(input("enter the x:"))
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
            print("Bad value")
    for i in range(0,len(number)):
        p = p + nember[i]*(x**i)
        if(i > 0):
            der = der + (i)*number[i]*(x**(i-1))
    print("Polynomial:",p)
    print("Derivative",der)
except FileNotFoundError:
    print("Can't open the file")
