
##SIMPLY RUN main() to get answers for all 3 cases.

#pythonic implementation of Djiikstras Algorithm using tuples and heap
  
from collections import defaultdict
from heapq import *

def main():
    driver(["Case1.txt", "Case2.txt", "Case3.txt"])

def answ(ans):
    for i in ans:
        if len(i)== 1:
            print(i[0])
        if len(i) > 1:
            print(i[0])
            return answ(i[1])

def dijkstra(edges, b, e):
    g = defaultdict(list)
    for f,l,m in edges:
        g[f].append((m,l))
    knew =  set()
    que = [(0,b,())]
    minu = {b: 0}
    while que:
        (cost,v1,path) = heappop(que)
        if v1 not in knew:
            knew.add(v1)
            path = (v1, path)
            if v1 == e:
                return (cost, path)
            for m, v2 in g.get(v1, ()):
                if v2 in knew: continue
                prev = minu.get(v2, None)
                next = cost + m
                if prev is None or next < prev:
                    minu[v2] = next
                    heappush(que, (next, v2, path))
    return float("inf")


def driver(fname):
    for i in range(0, len(fname)): 
        filename = fname[i]
        print(filename+ " ans:")
        file = open(filename, "r")
        graph=[]
        for line in file:
            line=line.split()
            if len(line) == 3:
                graph.append((line[0], line[1], int(line[2])))
        ans=[]
        ans.append(dijkstra(graph, "A", "B"))
        answ(ans)        
