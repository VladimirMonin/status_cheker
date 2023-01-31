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


# import notify2
# notify2.init('app name')
# n = notify2.Notification('title', 'message')
# n.show()

# import os


# def message_f(title, message):
#     os.system('notify-send "' + title + '" "' + message + '"')
#
#
# message_f(title, message)

# from tkinter import *
# import tkinter as tk
# from tkinter import messagebox
# root = tk.Tk()
# root.withdraw()
# messagebox.showwarning('alert title', 'Bad things happened!')

# import pyautogui as pag
# pag.alert(text="Bad things happened!", title="alert title")