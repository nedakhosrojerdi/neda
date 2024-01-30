def taqsim(num, den):
    num = num[:]  
    den = den[:]

    if len(num) < len(den):
        return [0], num  

    t = len(num) - len(den) 
    den = [0] * t + den

    quot = []
    j = float(den[-1])  

    i = 0
    while i <= t:
        mult = num[-1] / j
        quot = [mult] + quot
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)
        i += 1

    return quot, num 


print(taqsim([1,5,6], [1,2]))
