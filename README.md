# 711 寄件小幫手

<img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&logoWidth=24" alt=""/> 

![](https://i.imgur.com/IIRu4yy.jpg)

## 簡介

這是一個使用 Python 製作的小幫手，主要用來解決 711 店到店的繁瑣步驟，透過圖形化介面能夠輕鬆產生 QR Code，不須手動輸入。

## 主要功能

寄件人及收件人資訊可以在 `data.json` 中自行填入，在圖形化介面內會出現下拉選單可供選取收件人，QR Code 產生完畢後再點擊「下載 QR Code」按鈕，選取下載路徑即可。

## JSON 格式

格式如下，寄件人僅一名，收件人可自行增加。

```json
{
    "sender": {
        "Name": "寄件人姓名", 
        "Phone": "寄件人電話", 
        "Email": "寄件人信箱"
    },
    "receiver" : [
        {
            "Name": "收件人姓名", 
            "Phone": "收件人電話", 
            "Email": "收件人信箱",
            "ShopNumber": "取貨門市編號"
        }, {
            "Name": "收件人姓名", 
            "Phone": "收件人電話", 
            "Email": "收件人信箱",
            "ShopNumber": "取貨門市編號"
        }
    ]
}
```

## 備註

使用前請先將 data 資料夾中的 `data.exaple.json` 改為 `data.json` ，避免出錯。

711 門號可以至 [門市查詢](https://emap.pcsc.com.tw/)。
