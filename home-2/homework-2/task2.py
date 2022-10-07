txt = input()
t = 'a'
a = txt.split(" ")
for q in a:
        if len(q)>len(t):
            t=q
        else:
            continue
print(t)