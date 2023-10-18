# 2. RSA
# WITH INPUT
def gcd(a, b):
    rem = 0
    while True:
        rem = a % b
        if rem == 0:
            return b
        a = b
        b = rem


def primeFactors(a, b):
    c = 2
    while a > 1:
        if a % c == 0:
            b.append(c)
            a = a / c
        else:
            c = c + 1


def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups


message_raw = input("Input Message you want to Encrypt: ")
message_l = seperate_string_number(message_raw)
# print(message_l)
message_list = []
dic = {}
for i in message_l:
    try:
        message_list.append(int(i))
        dic[int(i)] = "True"
    except:
        for j in i:
            message_list.append(ord(j))
publickey = input("Input Public Key in format \"n, e\": ")
publickeystr = publickey.split(', ')
publickeylist = [eval(i) for i in publickeystr]
n1 = publickeylist[0]
e1 = publickeylist[1]
# print(message_list)
emsg1_list = [(i ** e1) % n1 for i in message_list]
# print(emsg1_list)
emsg2_list = [str(x) for x in emsg1_list]
emsg1 = "".join(emsg2_list)
print("Encrypted Message:", emsg1)
primefact = []
primeFactors(n1, primefact)
p1 = primefact[0]
q1 = primefact[1]
fi1 = (p1 - 1) * (q1 - 1)
d1 = pow(e1, -1, fi1)
emsg3_list = []
# print(emsg1_list)
# print(dic)
for i in emsg1_list:
    if (i ** d1) % n1 in dic:
        emsg3_list.append(str((i ** d1) % n1))
    else:
        emsg3_list.append(chr((i ** d1) % n1))
# print(emsg3_list)
dmsg = "".join(emsg3_list)
print("Decrypted Message:", dmsg)

# WITHOUT INPUT
import random


def gcd(a, b):
    rem = 0
    while True:
        rem = a % b
        if rem == 0:
            return b
        a = b
        b = rem


def primeFactors(a, b):
    c = 2
    while a > 1:
        if a % c == 0:
            b.append(c)
            a = a / c
        else:
            c = c + 1


def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups


p = int(input("Choose Prime Number 1: "))
q = int(input("Choose Prime Number 2 (different for Prime Number 1): "))
n = p * q  # public key
e = 2
fi = (p - 1) * (q - 1)
elist = []
while e < fi:
    if gcd(e, fi) == 1:
        elist.append(e)
        e = e + 1
    else:
        e = e + 1
sel_e = random.choice(elist)
msg = input("Input Message you want to Encrypt: ")
msg_l = seperate_string_number(msg)
msg_list = []
dic2 = {}
for i in msg_l:
    try:
        msg_list.append(int(i))
        dic2[int(i)] = "True"
    except:
        for j in i:
            msg_list.append(ord(j))
emsg1ex2_list = [(i ** sel_e) % n for i in msg_list]
emsg2ex2_list = [str(x) for x in emsg1ex2_list]
emsg1ex2 = "".join(emsg2ex2_list)
print("Encrypted Message:", emsg1ex2)
d1 = pow(sel_e, -1, fi)  # select e same as in first example => should give same encrypted message (inp = a111b, e = 14785, n = 74807, q = 239, p = 313)
emsg3_listex2 = []
for i in emsg1ex2_list:
    if (i ** d1) % n in dic2:
        emsg3_listex2.append(str((i ** d1) % n))
    else:
        emsg3_listex2.append(chr((i ** d1) % n))
# print(emsg3_listex2)
dmsg = "".join(emsg3_listex2)
print("Decrypted Message:", dmsg)
