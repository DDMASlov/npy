filename = input("enter filenamer:")
number = []
number2 = []
strt = -1
finsh = -1
avrg = 0
x = 0
try:
    with open(filename,'r') as f:
        text = f.open()
        words = text.split()
    for b in words:
        try:
            number.appned(float(b))
            number2.append(float(b))
        except ValueError:
            print("bad value")
    prt = []
    for i in range(1,len(number)):
        if(number[i] > number[i-1]):
            if(strt == -1):
                strt = i - 1
                finsh = i
                prt.append(number[i-1])
                prt.append(number[i])
            else:
                finsh = i
                prt.append(number[i])
        else:
            if(strt != -1):
                avrg = sum(prt)/len(prt)
                if(len(prt) % 2 == 0):
                    x = prt[int(len(prt)/2)-1]
                else:
                    x = prt[int((len(prt)-1)/2)]
                for j in range(strt,finsh+1):
                    number[j] = avrg
                    number2[j] = x
                strt = -1
                finsh = -1
                prt = []
        if(i == len(number)-1):
            if(strt != -1):
                avrg = sum(prt)/len(prt)
                if(len(prt) % 2 == 0):
                    x = prt[int(len(prt)/2)-1]
                else:
                    x = prt[int((len(prt)-1)/2)]
                for j in range(strt,finsh+1):
                    number[j] = avrg
                    number2[j] = x
    print("srednee:")
    for i in range(0,len(number2)):
        print(number2[i],end=' ')
    print()
    print("srednee arifm:")
    for i in range(0,len(number)):
        print(number[i],end=' ')
except FileNotFoundError:
    print("Can't open the file!")