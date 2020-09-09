def validation(s):
    u=set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-')
    w=set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    x=s.find("@")
    y=s.find(".")
    p=s[:x]
    q=s[x+1:y]
    r=s[y+1:]
    if(set(p).issubset(u) and set(q).issubset(w) and len(r) <= 3):
        return True
    else:
        return False
x = int(input("Enter the number of emails : "))
l=list(map(str,input().split()))
a = filter(validation,l)
r=[]
for i in a:
    r.append(i)
print(sorted(r))
