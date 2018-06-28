from fuzzywuzzy import fuzz, process

s = 'light brown sugar, firmly packed'
r1 = 'light brown sugar'
r2 = 'sugar'
r3 = 'brown sugar'
r4 = 'maple syrup'
r = [r1, r2, r3]

matches = []
for ri in r:
    score = fuzz.partial_token_set_ratio(s, ri)
    print(ri + ':\t %.2f' % score)
    if score == 100:
        matches.append(ri)

print(process.extractOne(s, matches, scorer=fuzz.token_set_ratio))
