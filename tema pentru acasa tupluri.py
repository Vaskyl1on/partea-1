def adunare(a,b):
    c=a+b
    return c
print(adunare(0,5))


def camparatie_5(x):
    if x > 5:
        return"mai mare"
    elif x < 5:
        return"mai mic"
    else:
        return"este egal"
x=input("Ce numar vreai sa compari cu 5:   ")
print (camparatie_5(x))