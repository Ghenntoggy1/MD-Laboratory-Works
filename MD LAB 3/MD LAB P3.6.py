# 3.6 Promote it
import pprint

interests_pe = []
with open('people_interests.txt') as f:
    for line in f:
        data = line.split()
        interests_pe.append(data[3:])
f.close()
# print(interests_pe)

with open('interests.txt') as f2:
    interests = [line.rstrip() for line in f2]
f2.close()
book_title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"
book_title_new = book_title.translate(str.maketrans('', '', ':,'))
title_list = book_title_new.split()
spectre = ['Books']
for word in title_list:
    for interest in interests:
        if word in interest:
            spectre.append(interest)
# print(spectre)
with open("NewRating.txt") as txt2:
    for line in txt2:
        rating = line.split(', ')
txt2.close()
newrating = [float(x) for x in rating]
# print(newrating)
with open('matrix.txt') as txt1:
    line = txt1.readline().strip('\n')
    names = line.split(" | ")
    names[0] = 'Caleb Hobby'
txt1.close()
# print(names)

coinc = []
for listpeople in interests_pe:
    x = list(set(spectre).intersection(listpeople))
    coinc.append(len(x))
# print(coinc)
list_coincrat = []
for i in range(len(coinc)):
    list_coincrat.append(0.2 * float(coinc[i]) * float(rating[i]))
# print(list_coincrat)
dict_namratefin = dict(zip(names, list_coincrat))
dict_sorted = {k: v for k, v in sorted(dict_namratefin.items(), key=lambda item: item[1], reverse=True)}
print('Top 5:')
for idx, (k, v) in enumerate(dict_sorted.items()):
    if idx == 5:
        break
    print(k, "-", v)
