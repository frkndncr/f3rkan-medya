from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import pyshorteners
import os

print("#######################################################")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                  İnsta: f3rrkan                       ")
print("                  Github: frkndncr                     ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("#######################################################")
print()

print("1.İnstagram Oturum Açma")
print("2.İnstagram Flood Araçı")
print("3.İnstagram Oto Dm Basıcı")
print("4.Twitter Oturum Açma")
print("5.İnstagram Brute Force")
print("6.Facebook Brute Force")
print("7.Url Kısaltma")
print("8.Phishing")
print()

islem = input("İşlem Numarası Giriniz: ")

if islem == "1":
    username = input("Kullanıcı Adı: ")
    password = input("Şifrenizi Giriniz: ")
    class Instagram:
        def __init__(self,username,password):
            self.browser = webdriver.Chrome()
            self.username = username
            self.password = password

        def singIn(self):
            self.browser.get("https://www.instagram.com/accounts/login/")
            time.sleep(2)

            usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
            passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(2)

        def dm(self):
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
            dm.click()
        
            dm = self.browser.get(f"https://www.instagram.com/{self.username}")

if islem == "2":
    username = input("Kullanıcı Adı: ")

    password = input("Şifrenizi Giriniz: ")

    metin = input("Metni Giriniz: ")

    basılcak = input("Flood Atılcak Kişi: ")
    class Instagram:
        def __init__(self,username,password):
            self.browser = webdriver.Chrome()
            self.username = username
            self.password = password

        def singIn(self):
            self.browser.get("https://www.instagram.com/accounts/login/")
            time.sleep(2)

            usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
            passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(4)

        def dm(self):
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
            dm.click()
            time.sleep(2)
            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            dm.click()
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
            dm.click()
         
            dmInput = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")

            dmInput.send_keys(f"{basılcak}")
            time.sleep(4)

        def msj(self):
            msj = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button")
            msj.click()
            time.sleep(3)
            msj = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
            msj.click()
            time.sleep(3)
         
        def oldu(self):
            msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
     
            msjInput.send_keys(f"{metin}")
            msjInput.send_keys(Keys.ENTER)
            time.sleep(0.5)

if islem =="3":
    username = input("Kullanıcı Adı: ")

    password = input("Şifrenizi Giriniz: ")

    hedef1 = input("Dm Basılcak 1. Kişinin Kullanıcı Adı: ")

    hedef2 = input("Dm Basılcak 2. Kişinin Kullanıcı Adı: ")

    metin = input("Metni Giriniz: ")
    class Instagram:
        def __init__(self,username,password):
            self.browser = webdriver.Chrome()
            self.username = username
            self.password = password

        def singIn(self):
            self.browser.get("https://www.instagram.com/accounts/login/")
            time.sleep(2)

            usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
            passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(4)

        def dm(self):
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
            dm.click()
            time.sleep(2)
            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            dm.click()
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
            dm.click()
         
            dmInput = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")

            dmInput.send_keys(f"{hedef1}")
            time.sleep(4)

            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button")
            dm.click()
            time.sleep(3)
            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
            dm.click()
            time.sleep(3)
         
            dmInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
     
            dmInput.send_keys(f"{metin}")
            dmInput.send_keys(Keys.ENTER)
            time.sleep(0.5)

            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
            dm.click()

            dmInput = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")

            dmInput.send_keys(f"{hedef2}")
            time.sleep(4)

            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button")
            dm.click()
            time.sleep(5)
         
            dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
            dm.click()
            time.sleep(3)
         
            dmInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
     
            dmInput.send_keys(f"{metin}")
            dmInput.send_keys(Keys.ENTER)
            time.sleep(0.5)

if islem =="4":
    username = input("Kullanıcı Adı: ")

    password = input("Şifrenizi Giriniz: ")
    class Instagram:
        def __init__(self,username,password):
            self.browser = webdriver.Chrome()
            self.username = username
            self.password = password

        def singIn(self):
            self.browser.get("https://twitter.com/login")
            time.sleep(2)

            usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
            passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(2)

        def dm(self):
            dm = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
            dm.click()

if islem =="5":
    os.system('git clone https://github.com/Bitwise-01/Instagram-')

if islem =="6":
    os.system('git clone https://github.com/Oseid/FaceBoom')
    os.system('git clone https://github.com/IAmBlackHacker/Facebook-BruteForce')

if islem =="7":
    def shorten(url):
        link = pyshorteners.Shortener()
        return link.tinyurl.short(url)

    if __name__ =="__main__":
        url = input("Enter Site Url: ")
        print(f"\nNew Link: {shorten(url)}")

if islem =="8":
    os.system('git clone https://github.com/suljot/shellphish')
    os.system('git clone https://github.com/An0nUD4Y/blackeye/')
    os.system('git clone https://github.com/yamanefkar/Turk-Sploit')
