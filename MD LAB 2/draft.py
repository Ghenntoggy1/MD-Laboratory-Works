
# # WITH INPUT
# choice = input("Choose Encryption(E, e, Encryption) or Decryption(D, d, Decryption): ")
# if choice == "Encryption" or choice == "E" or choice == "e":
#     message = int(input("Input Message you want to Encrypt: "))
#     publickey = input("Input Public Key in format \"n, e\": ")
#     publickeystr = publickey.split(', ')
#     publickeylist = [eval(i) for i in publickeystr]
#     n = publickeylist[0]
#     e = publickeylist[1]
#     emsg = (pow(message, e)) % n
#     print(emsg)
# elif choice == "Decryption" or choice == "D" or choice == "d":
#     message = int(input("Input Message you want to Decrypt: "))
#     privatekey = input("Input Private Key \"n, d\": ")
#     privatekeystr = privatekey.split(', ')
#     privatekeylist = [eval(i) for i in privatekeystr]
#     d = privatekeylist[1]
#     n = privatekeylist[0]
#     dmsg = (pow(message, d)) % n
#     print(dmsg)

# # WITHOUT INPUT
# import random
#
#
# def gcd(a, b):
#     rem = 0
#     while True:
#         rem = a % b
#         if rem == 0:
#             return b
#         a = b
#         b = rem
#
#
# def primeFactors(a, b):
#     c = 2
#     while a > 1:
#         if a % c == 0:
#             b.append(c)
#             a = a / c
#         else:
#             c = c + 1
#
#
# p = int(input("Choose Prime Number 1: "))
# q = int(input("Choose Prime Number 2 (different for Prime Number 1): "))
# n = p * q  # public key
# e = 2
# fi = (p - 1) * (q - 1)
# elist = []
# while e < fi:
#     if gcd(e, fi) == 1:
#         elist.append(e)
#         e = e + 1
#     else:
#         e = e + 1
# sel_e = random.choice(elist)
# msg = int(input("Input message: "))
# emsg = (pow(msg, sel_e)) % n
# print("Encrypted Message:", emsg)
# d = pow(sel_e, -1, fi)
# dmsg = (pow(emsg, d)) % n
# print("Decrypted Message:", dmsg)
# 2. RSA
# # WITH INPUT
# def gcd(a, b):
#     rem = 0
#     while True:
#         rem = a % b
#         if rem == 0:
#             return b
#         a = b
#         b = rem
#
#
# def primeFactors(a, b):
#     c = 2
#     while a > 1:
#         if a % c == 0:
#             b.append(c)
#             a = a / c
#         else:
#             c = c + 1
#
#
# message = int(input("Input Message you want to Encrypt: "))
# publickey = input("Input Public Key in format \"n, e\": ")
# publickeystr = publickey.split(', ')
# publickeylist = [eval(i) for i in publickeystr]
# n1 = publickeylist[0]
# e1 = publickeylist[1]
# emsg1 = (pow(message, e1)) % n1
# primefact = []
# primeFactors(n1, primefact)
# p1 = primefact[0]
# q1 = primefact[1]
# fi1 = (p1 - 1) * (q1 - 1)
# print("Encrypted Message:", emsg1)
# d1 = pow(e1, -1, fi1)
# dmsg = (pow(emsg1, d1)) % n1
# print("Decrypted Message:", dmsg)
#
#
# # WITHOUT INPUT
# import random
# def gcd(a, b):
#     rem = 0
#     while True:
#         rem = a % b
#         if rem == 0:
#             return b
#         a = b
#         b = rem
#
#
# def primeFactors(a, b):
#     c = 2
#     while a > 1:
#         if a % c == 0:
#             b.append(c)
#             a = a / c
#         else:
#             c = c + 1
#
#
# p = int(input("Choose Prime Number 1: "))
# q = int(input("Choose Prime Number 2 (different for Prime Number 1): "))
# n = p * q  # public key
# e = 2
# fi = (p-1)*(q-1)
# elist = []
# while e < fi:
#     if gcd(e, fi) == 1:
#         elist.append(e)
#         e = e + 1
#     else:
#         e = e + 1
# sel_e = random.choice(elist)
# msg = int(input("Input message: "))
# emsg = (pow(msg, sel_e)) % n
# print("Encrypted Message:", emsg)
# d = pow(sel_e, -1, fi)
# dmsg = (pow(emsg, d)) % n
# print("Decrypted Message:", dmsg)

# # WITH INPUT
# choice = input("Choose Encryption(E, e, Encryption) or Decryption(D, d, Decryption): ")
# if choice == "Encryption" or choice == "E" or choice == "e":
#     message = int(input("Input Message you want to Encrypt: "))
#     publickey = input("Input Public Key in format \"n, e\": ")
#     publickeystr = publickey.split(', ')
#     publickeylist = [eval(i) for i in publickeystr]
#     n = publickeylist[0]
#     e = publickeylist[1]
#     emsg = (pow(message, e)) % n
#     print(emsg)
# elif choice == "Decryption" or choice == "D" or choice == "d":
#     message = int(input("Input Message you want to Decrypt: "))
#     privatekey = input("Input Private Key \"n, d\": ")
#     privatekeystr = privatekey.split(', ')
#     privatekeylist = [eval(i) for i in privatekeystr]
#     d = privatekeylist[1]
#     n = privatekeylist[0]
#     dmsg = (pow(message, d)) % n
#     print(dmsg)

# WITH INPUT + string
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


message_raw = input("Input Message you want to Encrypt: ")
message_list = [ord(i) for i in message_raw]
publickey = input("Input Public Key in format \"n, e\": ")
publickeystr = publickey.split(', ')
publickeylist = [eval(i) for i in publickeystr]
n1 = publickeylist[0]
e1 = publickeylist[1]
emsg1_list = [(i ** e1) % n1 for i in message_list]
emsg2_list = [str(x) for x in emsg1_list]
emsg1 = "".join(emsg2_list)
print("Encrypted Message:", emsg1)
primefact = []
primeFactors(n1, primefact)
p1 = primefact[0]
q1 = primefact[1]
fi1 = (p1 - 1) * (q1 - 1)
d1 = pow(e1, -1, fi1)
emsg3_list = [chr((i ** d1) % n1) for i in emsg1_list]
dmsg = "".join(emsg3_list)
print("Decrypted Message:", dmsg)

# # BONUS. Mastermind
# s = str(input("Input Password: "))
# lower, upper, numeric, special = False, False, False, False
# s_chars = '~`!@#$%^&*()-_+={}[]|\;:"<>,./?'
# for ele in s:
#     if ele.islower():
#         lower = True
#     elif ele.isupper():
#         upper = True
#     elif ele.isdigit():
#         numeric = True
#     elif ele in s_chars:
#         special = True
# changes = 4 - (lower + upper + numeric + special)
# repeats = 0
# for i in range(0, len(s) - 2):
#     for ele in s:
#         if ele.islower():
#             lower = True
#         elif ele.isupper():
#             upper = True
#         elif ele.isdigit():
#             numeric = True
#         elif ele in s_chars:
#             special = True
#     if s[i] == s[i + 1] == s[i + 2]:
#         repeats += 1
#         if not special:
#             s = s[:i+2] + '{' + s[i+3:]
#         elif not numeric:
#             s = s[:i+2] + '0' + s[i+3:]
#         elif not upper:
#             s = s[:i + 2] +  + s[i + 3:]
#     print(s)
#     print(s[i], s[i + 1], s[i + 2])
# if repeats > 6:
#     repeats = 6
# if repeats > changes:
#     changes = repeats
# if 8 - len(s) >= changes:
#     changes = 8 - len(s)
# elif len(s) > 20:
#     changes = len(s) - 20 + changes
# # print(f"Steps: {changes if changes != 0 else 'good'}")
#
# if changes != 0:
#     print("Steps needed:", changes)
# else:
#     print("Strong")