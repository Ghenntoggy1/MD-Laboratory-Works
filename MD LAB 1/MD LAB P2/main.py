# 2. XNOR:
def xnor(a, b):
    print((not a and not b) or (a and b))


b1 = input("Boolean 1 = ")
b2 = input("Boolean 2 = ")
if (b1 == "True") or (b1 == "true") or (b1 == '1'):
    b1 = True
else:
    b1 = False
if (b2 == "True") or (b2 == "true") or (b2 == '1'):
    b2 = True
else:
    b2 = False

xnor(b1, b2)
