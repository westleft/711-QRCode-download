import tkinter as tk
import json
from download import crawler
from functools import partial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


file = open('data.json', 'r', encoding="utf-8")
data = json.loads(file.read())

class Gui():
    def __init__(self):
        window = tk.Tk()
        self.window = window
        window.title('711 店到店 QRCode 產生器')
        window.geometry(f'500x{len(data["receiver"] * 100)}')        

    def makeLabel(self):
        label= tk.Label(self.window, 
                        text= "歡迎使用711 店到店 QRCode 產生器，請選擇要寄送的客人：",
                        height='3',
                        width='50',
                        font=('微軟正黑體', 12)
                        )
        label.grid(column=0,row=0)

    def makeBtn(self):
        for index, item in enumerate(data['receiver']):
            btn = tk.Button(self.window, 
                            bg = '#FFC43D',
                            height = '2',
                            width = '20',
                            text = item['Name'], 
                            font = ('微軟正黑體', 12),
                            command = partial(crawler.run, index))
                            # command=partial(change_label_number, 2)
            btn.grid(column = 0, row = index + 1)

    def run(self):
        self.makeLabel()
        self.makeBtn()
        self.window.mainloop()

gui = Gui()
gui.run()