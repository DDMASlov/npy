import math
def area_on_vec(x1,y1,x2,y2):
    return math.fabs(x1*y2-y1*x2)/2
filename = input("enter filename:")
x = []
y = []
try:
    with open(filename,'r') as f:
        text = f.read()
        words = text.split()
    if(len(words)%2 != 0):
        print("Wrong number of coordinates!")
        exit()
    if(len(words) <= 4):
        print("There is not enough points!")
        exit()
    for i in range(0,len(words)):
        try:
            if(i % 2 == 0):
                x.append(float(words[i]))
            else:
                y.append(float(words[i]))
        except ValueError:
            print("bad value")
    minim = math.inf
    adr = [0,0,0]
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                dl = area_on_vec(x[i]-x[j],y[i]-y[j],x[i]-x[k],y[i]-y[k])
                if(dl < minim):
                    minim = dl
                    adr[0]=i
                    adr[1]=j
                    adr[2]=k
    print("area:",minim)
    print("first point:{",x[adr[0]],",",y[adr[0]],"}")
    print("second point: {",x[adr[1]],",",y[adr[1]],"}")
    print("third point: {",x[adr[2]],",",y[adr[2]],"}")
except FileNotFoundError:
    print("can't open the file!")