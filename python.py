import os
from random import randint
for i in range(1, 365):
    for j in range(0, randint(0, 8)):
        d = str(i+4) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add . ')
        os.system('git commit --date ="' + d + '" -m " commit " ')
os.system(' git push -u origin main ')
