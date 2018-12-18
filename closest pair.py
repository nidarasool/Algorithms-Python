from math import sqrt, pow

#finds the distance between closest pair of points from given data set

def dist(x, y):
  return sqrt(pow(x[0] - y[0],2) + pow(x[1] - y[1],2))

def minu(points, current=float("inf")):
  points=list(points)
  if len(points) < 2:
    return current
  else:
    head = points[0]
    del points[0]
    mina = min([dist(head, x) for x in points])
    newCurrent = min([mina, current])
    return minu(points, newCurrent)

def ClosestPair(fname):
    for i in range(0, len(fname)): 
        filename = fname[i]
        file = open(filename, "r")
        a=[]
        for line in file:
            line=line.split()
            inta=int(line[0])
            intb=int(line[1])
            a.append((inta, intb))
        b=list(a)
        if len(b) > 10:
          a=sorted(a)
        split = len(sorted(a))/2
        split=int(split)
        aa=minu(a[:split])
        ab=minu(a[:split])
        minimum = min([aa, ab])
        Line = filter(lambda x: x[0] > split - minimum and x[0] < split + minimum, a)
        ans= min([minu(Line), minimum])
        print(filename+" closest pair distnace: "+str(ans))


#RUN WITH FOLLOWING:
#fname=["10points.txt", "100points.txt", "1000points.txt"]
#print ClosestPair(fname)
