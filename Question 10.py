tup=(1,3,4,32,1,1,1)
t=0
for i in tup:
    if tup.count(i) > 1:
        t = t+1
        
print("Number of repeated items: ", t)
