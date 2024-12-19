from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


#from selenium.webdriver.common.keys import Keys
import time 

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
#time.sleep(3)
bot.maximize_window()

bot.get("https://www.viajesexito.com") #ingresar al sitio donde se tenga que hacer la automatizacion
time.sleep(1)

fly = bot.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
time.sleep(1.5)
fly.click()
time.sleep(1)

#origin
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(2)
origin.click()
origin_write = bot.find_element(By.ID,'popUpCityPredictiveFrom_netactica_airhotel')
origin_write.send_keys("Medellín")
time.sleep(2)
origin_airport = bot.find_element(By.XPATH, '//*[@id="ui-id-5"]/li/div/div[2]/p')
time.sleep(1)
origin_airport.click()
time.sleep(1)

#destination
destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
time.sleep(2)
destination.click()
destination_write = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
destination_write.send_keys("Cancún")
time.sleep(2)
destination_airport = bot.find_element(By.XPATH, '//*[@id="ui-id-6"]/li/div/div[2]')
time.sleep(1)
destination_airport.click()
time.sleep(1)

#departure date
select_departure_date = bot.find_element(By.XPATH, '//*[@id="Date_netactica_air_hotel"]')
time.sleep(2)
select_departure_date.click()
time.sleep(2)
departure_date = bot.find_element(By.XPATH, '//div[@aria-label="Sábado, Diciembre 21, 2024"]')
time.sleep(1)
departure_date.click()
time.sleep(4)

#Arrive date
arrive_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[6]/div[2]/div[1]')
time.sleep(3)
arrive_date.click()  

#Accept date
accept_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
time.sleep(3)
accept_date.click()
time.sleep(2)

#guests and rooms
rooms = bot.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
time.sleep(2)
rooms.click()
time.sleep(2)

#Add room
add_room = bot.find_element(By.XPATH, "//button[@id='btbAddRoomtwopaquetes']")
time.sleep(2)
add_room.click()
time.sleep(2)

add_adult = bot.find_element(By.XPATH, "//button[@class='btn btn-danger btn-number' and @data-type='plus' and @data-field='ddlAirHotelNumberAdultsDos']")
time.sleep(0.5)
add_adult.click()
add_adult.click()
time.sleep(2)

#Accept rooms
accept_room = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
time.sleep(1)
accept_room.click()
time.sleep(2)

#search
search = bot.find_element(By.XPATH, '//*[@id="sbm_netactica_airhotel"]')
time.sleep(1)
search.click()
time.sleep(5)

# new window
bot.switch_to.window(bot.window_handles[1])

#view packages
packages = WebDriverWait(bot, 10).until(
    ec.presence_of_all_elements_located(
        (By.XPATH, '//*[@id="divAirResults"]/div') 
    )
)

print("Packages")
print("")

for idx, package in enumerate(packages):
    
    price = package.find_element(By.XPATH, ".//span[contains(@class, 'currencyText')]")
    print(f"Package {idx + 1}: {price.text.strip()}")

print("")

time.sleep(30)

#Advance Options

advance_option = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
time.sleep(2)
advance_option.click()
time.sleep(5)

airline = WebDriverWait(bot, 10).until(
    ec.element_to_be_clickable((By.ID, 'txtAirlineCode'))
)

airline.click() 
time.sleep(1) 
airline.send_keys('Avianca')
time.sleep(1)
airline.send_keys(Keys.ENTER)
time.sleep(1)

#accept advance options
accept_advance_options = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
time.sleep(1)
accept_advance_options.click()
time.sleep(15)

#footer
footer = WebDriverWait(bot, 10).until(
    ec.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer')))

actions = ActionChains(bot)
actions.move_to_element(footer).perform()  
time.sleep(5)

#whatsapp
whatsapp = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
time.sleep(1)
whatsapp.click()
time.sleep(2)

bot.switch_to.window(bot.window_handles[2])

bot.close()  
bot.quit() 







