# 3.2 Sort

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
# print(names)
# dict = {}
# for name in names:
#     for number in friends:
#         dict[name] = number
#         friends.remove(number)
#         break
dict = dict(zip(names, friends))
# print(dict)
dict_sorted = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
for idx, (k, v) in enumerate(dict_sorted.items()):
    print(k, "-", v)
