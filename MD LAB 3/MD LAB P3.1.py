# 3.1 Friends

lines = []
friends = []
with open('matrix.txt') as f:
    line = f.readline().strip('\n')
    names = line.split(" | ")
    names[0] = 'Caleb Hobby'
    for i in f:
        x = i.count('1')
        friends.append(x)
f.close()
# dict = {}
# for name in names:
#     for number in friends:
#         dict[name] = number
#         friends.remove(number)
#         break
dict = dict(zip(names, friends))
# print(dict)
big = [name for name, number in dict.items() if number == max(dict.values())]
print(f"Most friends have: {', '.join(big)}", f"({max(dict.values())})")
