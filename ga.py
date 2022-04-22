import random

fl=[]       
fit = []    
prw = []    
po = []     
n = int(input("Enter the population size: ")) 

for x in range(0,n):                        
    a = random.randint(1, 10)
    if a<5:
        b = 5 - a;
    else:
        b = random.randint(1, 10)
    c = random.randint(1, 10)

    l = [a, b, c]  
    fl.append(l)    
    f = a + 2*b + 3*c - 5
    fit.append(f)   
    p = (1/f)*360
    prw.append(p)   


for i in range(0,n):
    s=0
    for j in range(0,i+1):
        s=s+prw[j]
    po.append(s)
    
print("Sets of values of [a,b,c]")   
print(fl)
print("\nFitness")
print(fit)
print("\nPercentage of each individual: ")
print(prw)
print("\nPercentage occupied on Roulette Wheel")
print(po)
print("\nBinary representation of [a,b,c]:");

be=[]   

for i in fl:   
    tl=[]       
    
    for j in i:     
        v=j         
        b=0
        p=1
        tl2=[]
        while v!=0:
            r =  v % 2
            b = b + r * p
            p = p * 10
            v = v // 2
            tl2.insert(0,r) 
        tl.append(tl2)          
    be.append(tl)               
print(be)

print("\nFour-bit binary representation of [a,b,c]:");

fbr=[]  
for i in be:
    nl1=[]
    t=[]
    for j in i:
        nl= []
        for k in j:
            
            nl.append(k)
            ll=len(nl)
                
        while ll<4:
            nl.insert(0,0)
            ll = len(nl)
            
        t.append(nl)
    fbr.append(t)
print(fbr)

print("\nRepresentation of each individual in 12 bits:")

ch = [] 
for i in fbr:
    tch = []
    for j in i:
        for k in j:
            tch.append(k)
    #print(tch)
    ch.append(tch)
print(ch)

gn=int(input("Enter the number of generation till which you want to run the algorithm: "))  
gc=1
while(gc<=gn):
    
    print("GENERATION ",gc)
    pa = [] 
    chn =[] 
    pin = []    
    k=1
    cp = 0.4*5  
    while k<=cp:
        rn = random.uniform(po[0],po[n-1])
        k = k+1
        pin.append(rn);
    
        for i in range(0,n):
            if rn < po[i]:
                chn.append(i-1)
                pa.append(ch[i-1])
                break
    print("\nPins generated: ")
    print(pin)
    print("Indices of selected parents: ")
    print(chn)
    print("\nParents chosen: ")
    print(pa)

    tp1 =[] 
    tp2 =[] 
    o1 = [] 
    o2 = [] 

    tp1 = pa[0]
    tp2 = pa[1]
    
    for i in range(0, 7):
        o1.append(tp1[i])
        o2.append(tp2[i])

    for j in range (7,12):
        o1.append(tp2[j])
        o2.append(tp1[j])
    
    print("\nOffsprings obtained after crossover: ")

    of=[]
    of.append(o1)
    of.append(o2)
    print(of)
    o =[]
    lfo=[]  

    for i in range(0,len(of)):
        o = of[i]
        a = 8*o[0]+ 4*o[1]+ 2*o[2]+ o[3];
        b = 8*o[4]+ 4*o[5]+ 2*o[6]+ o[7];
        c = 8*o[8]+ 4*o[9]+ 2*o[10]+ o[11];
    
        fo = a+2*b+3*c - 5  
        lfo.append(fo)
    print("\nCalculated Fitness of the offsprings: ")    
    print(lfo)


    for k in range(0,len(lfo)):
        max = fit[0]
        ind = 0
        for i in range(1,n):
            if fit[i]>max:
                max = fit[i]
                ind= fit.index(max)
        print("\nMaximum fitness: ",max)
        print("Position: ",ind)
        print("Initial fitness list");
        print(fit)
        if lfo[k]<max:
            fit[ind]=lfo[k]
            ch.pop(ind)
            ch.insert(ind, of[k])
        print("Fitness list after implementing minimisation:")
        print(fit)
        print("\nNew set of individuals: ")
        print(ch)
    gc = gc+1

