n = int(input("Enter the degree of the chndjomleii: "))
zarayb = []
i = 0
while i <= n:
    zarayb.append(float(input("Enter the zarayb of x^" + str(n-i) + ": ")))
    i += 1
chndjomleii = ""
i = 0
while i <= n:
    if i == n:
        chndjomleii += str(zarayb[i])
    elif i == n-1:
        chndjomleii += str(zarayb[i]) + "x + "
    else:
        chndjomleii +=f"{zarayb[i]}x^{n-i}+"
##        chndjomleii += str(zarayb[i]) + "x^" + str(n-i) + " + "
    i += 1
print("The chndjomleii is: " + chndjomleii)
##
##
##print(f"{zarayb[9]}x^9+{zarayb[8]}x^8+{zarayb[7]}x^7+{zarayb[6]}x^6+{zarayb[5]}x^5{zarayb[4]}x^4+{zarayb[3]}x^3+{zarayb[2]}x^2+{zarayb[1]}x+{zarayb[0]}")
