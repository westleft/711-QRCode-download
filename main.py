# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.filedialog import askdirectory
import tkinter as tk

from numpy import place
import requests
import time

from tools.reader import jsonReader
from tools.crawler import Crawler

class Application:
    def __init__(self):
        self.createTk()
        self.createTexts()
        self.createImage()
        self.createButtons()
        self.createRectangle()
        self.createOptionmenu()
        self.loopTk()

    # 產生 GUI 介面 & canvas
    def createTk(self):
        self.window = Tk()
        self.window.title("7-ELEVEN | 線上寄件 QRCODE 產生器")
        self.window.geometry("862x519")
        self.window.configure(bg="#1C2626")

        self.canvas = Canvas(
            self.window,
            bg="#1C2626",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

    # 建立文字
    def createTexts(self):
        # GUI 標題
        self.canvas.create_text(
            82.0, 42.0,
            anchor="nw",
            text="7-ELEVEN | 線上寄件 QRCODE 產生器",
            fill="#FFFFFF",
            font=("Tajawal Regular", 24 * -1)
        )

        self.canvas.create_text(
            48.0, 101.0,
            anchor="nw",
            text="請選取收件人",
            fill="#FFFFFF",
            font=("Tajawal Regular", 24 * -1)
        )

        self.canvas.create_text(
            567.0,
            316.0,
            anchor="nw",
            text="收件人姓名",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

        self.canvas.create_text(
            567.0,
            345.0,
            anchor="nw",
            text="收件人電話",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

        self.canvas.create_text(
            567.0,
            375.0,
            anchor="nw",
            text="收件人門市",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

        self.receiverName = self.canvas.create_text(
            652.0,
            316.0,
            anchor="nw",
            text="尚未選擇",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

        self.receiverPhone = self.canvas.create_text(
            652.0,
            345.0,
            anchor="nw",
            text="尚未選擇",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

        self.receiverShopNumber = self.canvas.create_text(
            652.0,
            375.0,
            anchor="nw",
            text="尚未選擇",
            fill="#FFFFFF",
            font=("Poppins Medium", 12 * -1)
        )

    # 建立按鈕
    def createButtons(self):
        # 產生 QR CODE
        Button(
            self.canvas, text="產生 QR CODE √",
            background="#552D96", fg="#fff",
            borderwidth=0, font=('微軟正黑體', 12),
            command = lambda: self.openCrawler()
        ).place(
            x = 48.0, y = 435.0,
            width = 461.0, height = 49.0
        )

        Button(
            self.canvas, text="取消",
            background="#445858", fg="#fff",
            borderwidth=0, font=('微軟正黑體', 12),
            command = lambda: self.window.destroy()
        ).place(
            x = 567.0, y = 434.0,
            width = 92.0, height = 49.0
        )

        Button(
            self.canvas, text="下載 QRCODE",
            background="#552D96", fg="#fff",
            borderwidth=0, font=('微軟正黑體', 12),
            command = lambda: self.downloadQrcode()
        ).place(
            x = 671.0, y = 434.0,
            width = 157.0, height = 49.0
        )
    
    def openCrawler(self):
        # 換圖片
        global qrcode
        qrcode = PhotoImage(file=r"assets/qqq.png")
        self.canvas.itemconfig(self.qrcode,image=qrcode)

        # =======
        print(self.receiver)
        crawler = Crawler(self.receiver)
        self.url = crawler.run()
        qrcode = PhotoImage(file=self.url)
        self.canvas.itemconfig(self.qrcode,image=qrcode)
    
    def downloadQrcode(self):
        path = askdirectory()
        # 取得下載路徑
        filename = path + f'/QRcode-{self.receiver["Name"]}{time.strftime("%Y-%m-%d", time.localtime())}.png'
        res = requests.get(self.url)
        with open(filename ,'wb') as f:
            f.write(res.content)

    # 建立圖片
    def createImage(self):
        global logo, qrcode
        logo = PhotoImage(file=r"assets/image_1.png")
        self.canvas.create_image(
            59.0, 51.0,
            image=logo
        )

        qrcode = PhotoImage(file=r"assets/image_2.png")
        self.qrcode = self.canvas.create_image(
            658.0,
            168.0,
            image=qrcode
        )

    # 建立下拉選單
    def createOptionmenu(self):
        # 取得下拉選單 收件人姓名
        jsonReader.readJson("./data/data.json")
        optionList = jsonReader.getReceiverName()

        var = tk.StringVar()
        var.set("請選擇收件人")
        myoptionmenu = tk.OptionMenu(self.window, var, *optionList)
        myoptionmenu.config(bg="#552D96", fg="WHITE")
        myoptionmenu["highlightthickness"] = 0
        myoptionmenu.place(
            x = 48.0,
            y = 150.0,
            width = 131.0,
            height = 41.0
        )
        # 觸發下拉選單事件
        var.trace("w", lambda *args: self.getOpitionValue(var.get()))

    # 下拉選單事件
    def getOpitionValue(self, value):
        self.receiver = jsonReader.filterData(value)
        self.canvas.itemconfig(self.receiverName, text = self.receiver['Name'])
        self.canvas.itemconfig(self.receiverPhone, text = self.receiver['Phone'])
        self.canvas.itemconfig(self.receiverShopNumber, text = self.receiver['ShopNumber'])

    # 建立矩形
    def createRectangle(self):
        self.canvas.create_rectangle(
            48.0,  77.0,
            515.0, 81.0,
            fill = "#9D73E3",
            outline = ""
        )

    # 持續執行 GUI 介面
    def loopTk(self):
        self.window.resizable(False, False)
        self.window.mainloop()


application = Application()