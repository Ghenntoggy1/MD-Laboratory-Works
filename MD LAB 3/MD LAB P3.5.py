# 3.5 Analyse your content
with open('interests.txt') as f:
    interests = [line.rstrip() for line in f]
f.close()
book_title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"
book_title_new = book_title.translate(str.maketrans('', '', ':,'))
title_list = book_title_new.split()
spectre = ['Books']
for word in title_list:
    for interest in interests:
        if word in interest:
            spectre.append(interest)
# print(title_list)
# print(interests)

print("Spectre of interest:", f"{', '.join(spectre)}")