def jam(chndjomleii1, chndjomleii2):
    degree = max(len(chndjomleii1), len(chndjomleii2))
    
    chndjomleii1 += [0] * (degree - len(chndjomleii1))
    chndjomleii2 += [0] * (degree - len(chndjomleii2))
    result = []
    i = 0
    while i < degree:
        result.append(chndjomleii1[i] + chndjomleii2[i])
        i += 1
    
    return result

def zarayb(ts):
    chndjomleii=""
    i = len(ts)-1
    while i >=0:
        if i == 0:
            chndjomleii += str(ts[i])
        elif i == 1:
            chndjomleii += str(ts[i]) + "x + "
        else:
            chndjomleii += str(ts[i]) + "x^" + str(i) + " + "
        i -= 1
    return chndjomleii



chndjomleii1=[2 ,5 ,9]
chndjomleii2=[3 ,5 ,6 ,8 ,9]
ts = jam(chndjomleii1, chndjomleii2)
gv = zarayb(ts)
print(gv)
