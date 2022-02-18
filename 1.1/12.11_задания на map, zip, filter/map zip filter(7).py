b=[1,2,3,4,5,6,1,2]
r=[4,5,6,1,2,3,9,1]
u=list(map(lambda x: x*2, r))
h=list(zip(b, u))
print(h)
