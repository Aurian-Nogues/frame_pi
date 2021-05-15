import os
# from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
import time
import pickle


# initialize selenium

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument("--disable-extensions")
options.add_argument("--disable-automation")
options.add_argument("--start-fullscreen")
options.add_argument("--kiosk")
options.add_experimental_option("excludeSwitches" , ["enable-automation"])
options.add_experimental_option("excludeSwitches" , ["enable-automation","load-extension"])
options.add_experimental_option('useAutomationExtension', False)

BASE_DIR = os.getcwd()
DISPLAY_DIR = os.path.join(BASE_DIR, 'display')
variables_path = os.path.join(DISPLAY_DIR, 'variables')


if os.path.isfile(variables_path) == False:
    print('Variables file does not exit, creating it')
    variables = {
        'wait_url': 'https://www.google.com',
        'display_url': None
    }
    file = open(variables_path, 'wb')
    pickle.dump(variables, file)
    file.close()
    latest_variables = variables

else:
    file = open(variables_path, 'rb')
    variables = pickle.load(file)
    file.close()
    latest_variables = variables

wait_url = variables['wait_url']
display_url = variables['display_url']

if display_url is None:
    active_url = variables['wait_url']
else:
    active_url = variables['display_url']

# display
driver = webdriver.Chrome(options=options) #Would like chrome to start in fullscreen
driver.get(active_url)

while True:
    time.sleep(1)

    file = open(variables_path, 'rb')
    variables = pickle.load(file)
    file.close()

    if variables != latest_variables:
        print('Received new display request')
        latest_variables=variables
        wait_url = variables['wait_url']
        display_url = variables['display_url']

        if display_url is None:
            active_url = variables['wait_url']
        else:
            active_url = variables['display_url']
        driver.get(active_url)



# url = 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/h/auto/100%25/%23000000'

# chrome_options = Options()
# chrome_options.add_experimental_option("useAutomationExtension", False)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument("--start-fullscreen");
# chrome_options.add_argument("--kiosk")

# # driver_path = os.path.join(os.getcwd(), 'display', 'chromedriver')
# # driver_path = '/usr/lib/chromium-browser/chromedriver'
# # print(driver_path)

# print('a')
# driver = webdriver.Chrome(options=chrome_options)
# # browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
# browser.get('www.google.com')
# print('b')

# driver_path = os.path.join(os.getcwd(), 'display', 'geckodriver')

# driver = webdriver.Firefox()
# driver.get('http://raspberrypi.stackexchange.com/')

# chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
# chromeOptions.addArguments("disable-infobars")
# driver = webdriver.Chrome(chrome_options=chromeOptions) #Would like chrome to start in fullscreen
# driver.get("https://www.google.com")

# options = webdriver.ChromeOptions()

# # options.add_argument('--no-sandbox')
# # options.add_argument('--disable-dev-shm-usage')

# options.add_argument('--start-maximized')
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-automation")
# options.add_argument("--start-fullscreen")
# options.add_argument("--kiosk")
# options.add_experimental_option("excludeSwitches" , ["enable-automation"])
# options.add_experimental_option("excludeSwitches" , ["enable-automation","load-extension"])
# options.add_experimental_option('useAutomationExtension', False)

# driver = webdriver.Chrome(options=options) #Would like chrome to start in fullscreen
# driver.get(url)
