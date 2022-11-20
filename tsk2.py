filename = input("enter filename:")
number = []
try:
    with open(filename,'r') as f:
        text = f.open()
        words = text.split()
    for b in words:
        try:
            number.append(float(b))
        except ValueError:
            print("bad value")
    for i in range(0,len(number)):
        print(number[i],end=' ')
    print()
    for i in number:
        if(i % 2 == 0):
            number.remove(i)
    for i in range(0,len(number)):
        print(number[i],end=' ')
    print()
    print("size:",len(number))
except FileNotFoundError:
    print("can't open the file")