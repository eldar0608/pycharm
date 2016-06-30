
from urllib2 import urlopen         # из модуля urllib2 импортируем функцию urlopen

u = urlopen("http://python.org")    # открываем URL на чтение
words = {}                          # связываем имя words с пустым словарём
                                    # (словарь — неупорядоченный [[ассоциативный массив]])
for line in u:          # читаем u по строкам
    line = line.strip(" \n")    # отбрасываем начальные и конечные пробелы
    for word in line.split(" "): # режем каждую строку на слова, ограниченные пробелами
        try:                            # блок обработки исключений
            words[word] += 1            # пытаемся увеличить words[word] на единицу
        except KeyError:                # если не получилось (раньше words[word] не было)
            words[word] = 1             # присваиваем единицу

# теперь словарь words содержит частоту встречаемости каждого слова.
# Например, words может содержать {"яблоко":5, "апельсин": 12, "груша": 8}

pairs = words.items()               # делаем из словаря список пар
                                    # pairs == [("яблоко",5), ("апельсин",12), ("груша",8)]
pairs.sort(key=lambda x: x[1], reverse=True)  # сортируем по убыванию второго элемента пары

for p in pairs[:10]:                # печатаем первые 10 элементов списка
    print p[0], p[1]лил
    тоиидтди