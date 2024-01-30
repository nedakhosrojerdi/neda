def moshtaq(chndjomleii, n):
    if n == 0:
        return chndjomleii
    else:
        result = chndjomleii[:]
        count = 0
        while count < n:
            temp = [0] * (len(result) - 1)
            i = 0
            while i < len(temp):
                temp[i] = result[i] * (len(result)-i - 1)
                i += 1
            result = temp
            count += 1
        return result

chndjomleii=[5,2,3,5]
n=2
ts=moshtaq(chndjomleii, n)
print(ts)
