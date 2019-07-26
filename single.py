def f1(a,p):
    if a-p>p:
        p=a-p-1
    return p-int(a/2)
for x in range(int(input())):
    a, b = map(int, input().split())
    cmax=-1
    cc=999
    for i in range(a):
        for j,v in enumerate(list(map(int, input().split()))):
          dd=f1(a,i)+f1(b,j)
          if v>cmax or (v==cmax and cc>dd):
            cc=dd
            cmax=v
    print(cc)
