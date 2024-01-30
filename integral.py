def integral(chndjomleii, n):
    result = chndjomleii[:]
    count = 0
    while count < n:
        temp = [0] * (len(result) + 1)
        temp[0] = 0
        i = 0
        while i < len(result):
            temp[i+1] = result[i] / (i + 1)
            i += 1
        result = temp
        count += 1
    return result

chndjomleii=[1,2]
n=1
ts=integral(chndjomleii, n)
print(ts)
