#!/usr/bin/env python
import sys

# читаем из стандартного входа
for line in sys.stdin:  # для каждой посткпающейе строки
    # удаляем пробелы в начале и конце строки
    line = line.strip()
    # разбиваем строчку на слова
    words = line.split()
    # наращиваем счётчики
    for word in words:
        #  пишем результат в стандартный поток вывода
        # - выход мэппера будем входом
        #   редуктора reducer.py
        #
        # разделям табом слово и назначаем ему число вхождений 1
        print(word, 1)