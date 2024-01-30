n = int(input("Enter the degree of the chndjomleii: "))
zarayb = []
i = 0
while i <= n:
    zarayb.append(float(input("Enter the zarayb of x^" + str(n-i) + ": ")))
    i += 1
x=float(input("x0:"))
chndjomleii = 0
i = 0
while i <= n:
    j=n-i
    chndjomleii += zarayb[i] * x**j 
    i += 1
print(f"f({x}): {chndjomleii}")
