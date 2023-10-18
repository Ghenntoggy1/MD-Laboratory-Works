# 4.3 Top
import json
import nltk
import contractions
import re

f = open('tweets.json', "r", encoding='utf-8')
data = json.loads(f.read())
f.close()
text = []
orig = {}
for text_field in data:
    idl = text_field['id']
    clrtxt = text_field['text']
    orig[idl] = clrtxt
    clrtxt = clrtxt.replace('\n', ' ')
    clrtxt = clrtxt.replace('RT', '')
    clrtxt = re.sub(r'http\S+', '', clrtxt)
    clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
    clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
    clrtxt = contractions.fix(clrtxt)
    text.append(clrtxt.lower())

# print(text)
string_list = []
for string in text:
    str1 = nltk.RegexpTokenizer(r"\w+")
    str2 = str1.tokenize(string)
    string_list.append(str2)

for list2 in string_list:
    for i in range(len(list2)):
        if list2[i] == 'cannot':
            list2[i] = "can't"
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'some' and list2[i+1] == 'kind':
            list2[i] = 'some kind'
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'not' and list2[i+1] == 'good':
            list2[i] = 'not good'
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'not' and list2[i+1] == 'working':
            list2[i] = 'not working'
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == "do" and list2[i+1] == 'not':
            list2[i] = "dont"
            list2.remove(list2[i+1])
            break
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'dont' and list2[i+1] == 'like':
            list2[i] = "dont like"
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'no' and list2[i+1] == 'fun':
            list2[i] = 'no fun'
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 1):
        if list2[i] == 'screwed' and list2[i+1] == 'up':
            list2[i] = 'screwed up'
            list2.remove(list2[i+1])
for list2 in string_list:
    for i in range(len(list2) - 2):
        if list2[i] == 'does' and list2[i+1] == 'not' and list2[i+2] == 'work':
            list2[i] = 'does not work'
            list2.remove(list2[i+1])
            list2.remove(list2[i+1])
# print(string_list)
id_list = []
for id_field in data:
    id = id_field['id']
    id_list.append(id)
# print(id_list)

dic_idword = dict(zip(id_list, string_list))
# print(dic_idword)

affinn = {}
with open('AFINN-111.txt') as txt:
    data_txt = txt.read().splitlines()
txt.close()
for i in data_txt:
    x = i.split()
    val = int(x[len(x) - 1])
    del x[len(x) - 1]
    word = x[0]
    del x[0]
    for j in x:
        word += " " + j
    affinn[word] = val
# print(affinn)

rating_list = []
dict_idrating = {}
for tweet in dic_idword.values():
    rating = 0
    for word in tweet:
        if word in affinn:
            rating += affinn[word]
    rating_list.append(rating)
    dict_idrating[list(dic_idword.keys())[list(dic_idword.values()).index(tweet)]] = rating

dict_sorted = {k: v for k, v in sorted(dict_idrating.items(), key=lambda item: item[1], reverse=True)}
print("TOP 10 MOST POSITIVE TWEETS:")
for idx, (k, v) in enumerate(dict_sorted.items()):
    if idx == 10:
        break
    print('-' * 170)
    print("ID:", k, orig[k], "\nRating :", v)

dict_sorted2 = {k: v for k, v in sorted(dict_idrating.items(), key=lambda item: item[1])}
print("+"*170)
print("+"*170)
print("+"*170)
print("TOP 10 MOST NEGATIVE TWEETS:")
for idx, (k, v) in enumerate(dict_sorted2.items()):
    if idx == 10:
        break
    print('-'*170)
    print("ID:", k, ":", orig[k], "\nRating :", v)