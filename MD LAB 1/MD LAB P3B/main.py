# 3B. Longest substring B:
def repeat(s):
    substrs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrs.append(s[i: j])
    substrs_list = list(substrs)
    for i in substrs_list:
        if len(i) > len(set(i)):
            substrs.remove(i)
    print(len(max(set(substrs), key=len)))


string = input()
repeat(string)
