from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 使用按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

chromedriver = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

sender = {
    'Name': '吳薯條', 
    'Phone': '0933545545', 
    'Email': 'wow12399@gmail.com'}
receiver = {
    'Name': '吳薯條', 
    'Phone': '0933545545', 
    'Email': 'wow12399@gmail.com'}

class Crawler():
    def __init__(self):
        self.driver = webdriver.Chrome(service = chromedriver, options=options)
        self.driver.maximize_window()
    def goToWebsite(self):
        self.driver.get('https://myship2.7-11.com.tw/C2C/Page02')

    def page02(self):  
        self.driver.find_element_by_xpath('//*[@id="shippingValue"]').click()
        self.driver.find_element_by_xpath('//*[@id="shippingValue"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="orderAmount"]').send_keys('999')
        self.driver.find_element_by_xpath('//*[@id="nextStep"]').click()

    def page03(self):
        for index,(key, value) in enumerate(sender.items()):
            self.driver.find_element_by_xpath(f'//*[@id="sender{key}"]').send_keys(value)

        self.driver.find_element_by_xpath('//*[@id="nextStep"]').click()

    def page04(self):
        for index,(key, value) in enumerate(receiver.items()):
            self.driver.find_element_by_xpath(f'//*[@id="receiver{key}"]').send_keys(value)

        self.driver.find_element_by_xpath('//*[@id="checkStore"]').click()   
        
    def selectStore(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_xpath('//*[@id="byID"]').click()

        self.driver.switch_to.frame('frmMain')

        self.driver.find_element_by_xpath('//*[@id="storeIDKey"]').send_keys('174109')
        self.driver.find_element_by_xpath('//*[@id="send"]').click()

        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ol_stores"]/li'))
            )
            self.driver.find_element_by_xpath('//*[@id="ol_stores"]/li').click()
        finally:
            pass

        self.driver.switch_to.parent_frame()
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sevenDataBtn"]'))
            )
            self.driver.find_element_by_xpath('//*[@id="sevenDataBtn"]').click()
        finally:
            pass
        
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="AcceptBtn"]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="submit_butn"]').click()
        
        window_after = self.driver.window_handles[0]
        self.driver.switch_to.window(window_after)

        self.driver.find_element_by_xpath('//*[@id="nextStep"]').click()

    def page05(self):
        self.driver.find_element_by_xpath('//*[@id="printOrder"]').click()

    def downloadQRcode(self):
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.ID, 'pinno'))
            )
            time.sleep(3)
        finally:
            pass
        urlNumber = self.driver.find_element_by_id('pinno').text

        res = requests.get(f'https://epayment.7-11.com.tw/C2C/C2CWeb/QRCode.ashx?CodeValue={urlNumber}')
        with open(f'QRcode-{time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())}.png' ,'wb') as f:
            f.write(res.content)

    def run(self):
        self.goToWebsite()
        self.page02()
        self.page03()
        self.page04()
        self.selectStore()
        self.page05()
        self.downloadQRcode()

crawler = Crawler()
crawler.run()