def jam(chndjomleii1, chndjomleii2):
    degree = max(len(chndjomleii1), len(chndjomleii2))
    
    chndjomleii1 += [0] * (degree - len(chndjomleii1))
    chndjomleii2 += [0] * (degree - len(chndjomleii2))
    result = []
    i = 0
    while i < degree:
        result.append(chndjomleii1[i] + chndjomleii2[i])
        i += 1
