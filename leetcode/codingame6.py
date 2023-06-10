# a*x + b = y


# input
s =  "2 * x  + 2 = 8"

s = s.replace(" ", "")

a = float(s[0])
b = float(s[4])
y = float(s[-1])

x = (y-b)//a

print(int(x))