from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys
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

#origin
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(3)
origin.click()
originwrite = bot.find_element(By.ID,'popUpCityPredictiveFrom_netactica_airhotel')
originwrite.send_keys("Medellín")
time.sleep(3)
origin_airport = bot.find_element(By.XPATH, '//*[@id="ui-id-5"]/li/div/div[2]/p')
time.sleep(1)
origin_airport.click()
time.sleep(1)

#destination
destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
time.sleep(3)
destination.click()
destinationwrite = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
destinationwrite.send_keys("Cancún")
time.sleep(3)
destination_airport = bot.find_element(By.XPATH, '//*[@id="ui-id-6"]/li/div/div[2]')
time.sleep(1)
destination_airport.click()
time.sleep(1)












'''
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(2)
origin.click()
/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]

advertisement = bot.find_element(By.XPATH,'/html/body/div/div/div/div[1]/svg/path')
time.sleep(2)
advertisement.click()
time.sleep(2)


origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(3)
origin.click()

inputorigin = "Medellin"
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(3)
origin.click()
origin.send_keys(inputorigin)
time.sleep(3)

'''

