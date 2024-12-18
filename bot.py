from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
#time.sleep(3)
bot.maximize_window()

bot.get("https://www.viajesexito.com") #ingresar al sitio donde se tenga que hacer la automatizacion
time.sleep(1)


fly = bot.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
time.sleep(2)
fly.click()
time.sleep(2)




'''
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(2)
origin.click()
/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]

advertisement = bot.find_element(By.XPATH,'/html/body/div/div/div/div[1]/svg/path')
time.sleep(2)
advertisement.click()
time.sleep(2)
'''

