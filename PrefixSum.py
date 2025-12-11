a = [8,3,-2,4,10,-1,0,5,3]
p = [a[0]]

for i in range(1,len(a)):
    p.append(p[i-1] + a[i])

print(a)
print(p)

#suppose if they ask from a[l,r] => l=2 , r=7

l = 2
r = 7
print(p[r] - p[l-1])

#here is l=0 then??

a = [8,3,-2,4,10,-1,0,5,3]

pp=[]
pp = [0]

for i in range(0,len(a)):
    pp.append(pp[i] + a[i])

print(a)
print(pp)

#suppose if they ask from a[l,r] => l=2 , r=7

l = 2
r = 7
print(pp[r+1] - pp[l])