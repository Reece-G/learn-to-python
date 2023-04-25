def chop(x):
    del x[0]
    del x[-1]

def middle(x):
    mid = x[1:-1]
    return mid

t = [1,2,3,4,5]
y = [42, 60, 70, 80]

chop(t)
print(t)
mid = middle(y)
print(mid)
