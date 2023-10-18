# 4.1 Popular Hashtag
from collections import Counter
import json
import re

f = open('tweets.json', "r", encoding='utf-8')
data = json.loads(f.read())
f.close()
freq = Counter()
text = []
for text_field in data:
    x = re.findall('#[A-Za-z0-9]+', text_field['text'])
    if x:
        text.append(x)
resultlist = sum(text, [])
# print(resultlist)
c = Counter(resultlist)
x = c.most_common(10)
for i in x:
    print(f"{''.join(i[0])} - {''.join(str(i[1]))}")
