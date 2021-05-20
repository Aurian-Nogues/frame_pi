import os
# from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
import time
import pickle
import subprocess


# initialize selenium

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument("--disable-extensions")
options.add_argument("--disable-automation")
options.add_argument("--start-fullscreen")
options.add_argument("--kiosk")
options.add_argument("--hide-scrollbars")
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
        'display_url': None,
        'orientation':'h'
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
orientation = variables['orientation']

if display_url is None:
    active_url = variables['wait_url']
else:
    active_url = variables['display_url']

# get display to right inclination
if orientation == 'h':
    x = subprocess.run(['xrandr', '-o', 'normal'])
else:
    x = subprocess.run(['xrandr', '-o', 'right'])

# display
driver = webdriver.Chrome(options=options)
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
        orientation = variables['orientation']


        if orientation == 'h':
            x = subprocess.run(['xrandr', '-o', 'normal'])
        else:
            x = subprocess.run(['xrandr', '-o', 'right'])


        if display_url is None:
            active_url = variables['wait_url']
        else:
            active_url = variables['display_url']



        
        driver.get(active_url)

