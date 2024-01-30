def x0(poly,x):
    i=0
    f=0
    while i<len(poly):
        f+=poly[i]*x**(len(poly)-i-1)
        i+=1
    return f



def rishe(poly, a, b, khata=1e-6):
    if x0(poly, a) * x0(poly, b) > 0:
        return None  

    i= 1
    while i <= 100:
        c = (a + b) / 2
        if abs(x0(poly, c)) < khata:
            return c
        
        if x0(poly, a) * x0(poly, c) < 0:
            b = c
        else:
            a = c
        i += 1

    if i > 100:
            return nashod  

poly=[1,2,-3]
a=0
b=4
ts=rishe(poly, a, b, khata=1e-6)
print(ts)
