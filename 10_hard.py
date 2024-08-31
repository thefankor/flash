import re

f = open('demo_2025_10.txt')
text = f.read().lower()     # Читаем данные из файла и переводим все буквы в нижний регистр

words = re.findall(r'\b[а-яё]{5,}\b', text)     # Ищем слова и сохраняем их в words

word_counts = {}  
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # Если слово уже есть в словаре, увеличиваем его счетчик
    else:
        word_counts[word] = 1  # Если слово встречается впервые, добавляем его в словарь со значением 1

most_frequent_word = None  
max_count = 0  
for word, count in word_counts.items():
    if count > max_count:  # Сравниваем текущее количество вхождений с максимальным
        max_count = count  # Обновляем максимальное количество вхождений
        most_frequent_word = word  # Обновляем самое часто встречающееся слово

print(most_frequent_word)  # Возвращаем самое часто встречающееся слово