# 4. Palindrome
str = input("String: ")
charlist = []
j = 0
for i in str:
    charlist.append(i)
for i in range(len(charlist)):
    if charlist[i] != charlist[-i-1]:
        charlist.insert(j, charlist[-j-1])
        j += 1
palindrome = ''.join(charlist)
print("Formed Palindrome:", palindrome)
