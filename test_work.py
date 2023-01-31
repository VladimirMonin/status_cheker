# КОД ОБРАЩЕНИЯ НА ЛЕНДИНГИ

import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen("https://noukash.com/intensive").read().decode('utf-8')

soup = BeautifulSoup(response, "html.parser")
text = soup.body.get_text().strip()

if "Ниже форма предзаписи" in text:
    print('Предзапись ещё открыта')

# Код взят тут:  https://stackoverflow.com/questions/27803503/get-html-using-python-requests

# КОД УВЕДОМЛЕНИЙ


import os

command = f'''notify-send'''
os.system(command)