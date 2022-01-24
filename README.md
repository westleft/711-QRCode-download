# 711 店到店 QRCode 產生器

![](https://img.shields.io/badge/Python-exercise-%23336d9b)

![](https://i.imgur.com/PCa7K33.png)


每次使用 711 店到店都要輸入寄件人資料 / 收件人資料 / 選門市...等資訊，太麻煩了。所以利用 `selenium` 幫忙填入資料，並將最終產生的 QR Code 下載下來。
為了避免檔名混淆也增加了收件者姓名 & 當日時間 (年月日時分秒)。

這次遇到的問題有：

## 彈出視窗及 iframe
遇到彈跳視窗直接使用 `window_handles` 並控制，iframe 則是 `switch_to.frame`。

## 學習到的知識
使用 `enumerate` 搭配 `for` 可以產生像 JS 中的 `foreach` 用法

```python
for index, itme in enumerate(sender):
```

如果是 `dictionary` 則加個 `()` 以及 `.items()` 即可
```python
for index,(key, value) in enumerate(sender.items()):
```

## 預計修正項目
* ~~使用 GUI~~(已完成)
* 寄件及收件人資訊獨立檔案，並增加修改功能
* 目前使用 `json` 儲存資料，改用資料庫
* 打包成 exe

過程中有使用 `try` 的用法，等待元素出現再執行
```python
try:
    WebDriverWait(self.driver, 4).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sevenDataBtn"]'))
    )
finally:
    pass
```
不過有些元素是本來就已經存在在網頁上，只是被使用了 `display: none`。這邊暫時用了 `tiem.sleep()` 強制等待，未來有更好的方法再修正。