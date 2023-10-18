# 3A. Longest substring A:
from collections import Counter


def repeat(s):
    substrs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrs.append(s[i: j])
    # subs = {}
    print(substrs)
    subs = Counter(substrs)
    key_list = []
    print(subs)
    for key, value in subs.items():
        if len(key) != 1:
            key_list.append(key)
    key_list.remove(s)
    # print(key_list)
    key_list_dict = {}
    for i in key_list:
        c = s.count(i)
        key_list_dict[i] = c
    # print(key_list_dict)
    val_list = list(key_list_dict.values())
    print(val_list)
    x = max(val_list)
    # print(x)
    key_list_2 = []
    for key, value in subs.items():
        if x == value:
            key_list_2.append(key)
    print(key_list_2)
    p = max(key_list_2, key=len)
    if p == s:
        print("\"\"")
    elif x == 1:
        print("\"\"")
    else:
        print(p)


string = input()
repeat(string)
