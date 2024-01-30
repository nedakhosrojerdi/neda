def zarb(chndjomleii1, chndjomleii2):
    darje1 = len(chndjomleii1) - 1
    darje2 = len(chndjomleii2) - 1
    result_daraje = darje1 + darje2
    result = [0] * (result_daraje + 1)
    
    i = 0
    while i <= darje1:
        j = 0
        while j <= darje2:
            result[i + j] += chndjomleii1[i] * chndjomleii2[j]
            j += 1
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


chndjomleii1=[1,1]
chndjomleii2=[1,-1]
ts = zarb(chndjomleii1, chndjomleii2)
gv = zarayb(ts)
print(gv)

