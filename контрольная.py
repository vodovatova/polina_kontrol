# задание на 5 баллов

import re
from bs4 import BeautifulSoup
import pickle

import os
import glob

newdict = {}

os.chdir("/Users/polinavodovatova/Downloads/thai_pages/")
for file in glob.glob("*.srctext"):
        f = open(file)
        srctext = f.read()
        f.close()

        ParsingObj = BeautifulSoup(srctext, 'lxml')

        thaitable = ParsingObj.find("table", {"class":"gridtable"})

        for row in thaitable.tr.next_siblings:
            try:
                thaiword = row.find('a', href=re.compile('^/id/\S*')).get_text()
            except:
                continue
            components = []
            for item in row.td.next_siblings:
                try:
                    text = item.get_text()
                    components.append(text)
                except:
                    continue
            newdict[thaiword] = components[-1]

print('Словарь')
print('Получаем словарь из', len(newdict), 'элементов')
f = open('NewDict.dic', 'wb')
pickle.dump(newdict, f)
f.close()
