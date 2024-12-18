from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time 

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
time.sleep(3)
bot.maximize_window()
time.sleep(3)

bot.get("https://www.viajesexito.com") #ingresar al sitio donde se tenga que hacer la automatizacion
time.sleep(1)