import re

f = open('demo_2025_10.txt')
text = f.read().lower()

words = re.findall(r'\b[а-яё]+\b', text)

maxlen = 0
for w in words:
    if len(w) > maxlen:
        maxlen = len(w)
print(maxlen)