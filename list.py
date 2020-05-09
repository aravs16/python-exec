l = ['s','a','i']
m = ['v','a','m','s','h','i']

for i in l[:]:
    if i in m:
        l.remove(i)
        m.remove(i)

print(l,m)