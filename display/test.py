import pathlib
import os
# from selenium.webdriver.chrome.options import Options  
from selenium import webdriver


url = 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/h/auto/100%25/%23000000'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--start-fullscreen");
chrome_options.add_argument("--kiosk")

# driver_path = os.path.join(os.getcwd(), 'display', 'chromedriver')
driver_path = '/usr/lib/chromium-browser/chromedriver'
print(driver_path)

print('a')
# driver = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
browser.get(url)
print('b')

# driver_path = os.path.join(os.getcwd(), 'display', 'geckodriver')

# driver = webdriver.Firefox()
# driver.get('http://raspberrypi.stackexchange.com/')