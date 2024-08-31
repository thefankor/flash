import re

f = open('demo_2025_10.txt')
text = f.read().lower()

words = re.findall(r'\bз[а-яё]*я\b', text)
print(len(words))