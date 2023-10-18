# 3.4 Influential people
import pprint

list = []
with open('matrixSPT3-3.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(', ')]
        list.append(inner_list)
f.close()

influence = []
with open('influence.txt') as txt:
    for line in txt:
        data = line.split()
        influence.append(data[3])
txt.close()
# print(influence)
with open('matrix.txt') as txt2:
    line = txt2.readline().strip('\n')
    names = line.split(" | ")
    names[0] = 'Caleb Hobby'
txt2.close()
# print(names)
rating = []
for i in list:
    r = 0
    for j in i:
        r += j
    rating.append(r)
# print(rating)
# for i in matrixSPT2:
#     r = 0
#     for j in i:
#         if j != 0:
#             r += j - 1
#         else:
#             r += j
#     rating.append(r)
# dic = {}
dict1 = dict(zip(influence, rating))

brand = []
for x, y in dict1.items():
    brand.append(0.5 * float(x) * float(y))
# print(brand)
dict_brand = dict(zip(names, brand))
dict_sorted = {k: v for k, v in sorted(dict_brand.items(), key=lambda item: item[1], reverse=True)}
for idx, (k, v) in enumerate(dict_sorted.items()):
    print(k, "-", v)

with open('NewRating.txt', 'w') as ll:
    ll.write(str(brand)[1:-1])
ll.close()