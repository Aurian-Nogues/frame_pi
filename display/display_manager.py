import os
# from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
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
PAGES_DIR = os.path.join(BASE_DIR, 'display', 'pages')
variables_path = os.path.join(DISPLAY_DIR, 'variables')
wait_page_path = os.path.join(PAGES_DIR, 'waiting_page.html')
no_wifi_url = os.path.join(PAGES_DIR, 'no_wifi.html')

def trigger_display(driver, latest_variables):
    file = open(variables_path, 'rb')
    variables = pickle.load(file)
    file.close()

    if variables != latest_variables:
        latest_variables = variables

        wait_url = variables['wait_url']
        no_wifi_url = variables['no_wifi_url']
        wifi_connected = variables['wifi_connected']
        display_url = variables['display_url']
        orientation = variables['orientation']

        if wifi_connected is False:
            active_url = no_wifi_url
        else:
            if display_url is None:
                active_url = variables['wait_url']
            else:
                active_url = variables['display_url']

        if orientation == 'h':
            x = subprocess.run(['xrandr', '-o', 'normal'])
        else:
            x = subprocess.run(['xrandr', '-o', 'right'])

        try:
            driver.get(active_url)
        except WebDriverException:
            driver.get(no_wifi_url)
    
    return latest_variables


def main():
    if os.path.isfile(variables_path) == False:
        
        # create default variables file
        print('Variables file does not exit, creating it')
        variables = {
            'wait_url': 'file://' + wait_page_path, # need this prefix when loading from local drive
            'no_wifi_url' : 'file://' + no_wifi_url,
            'wifi_connected' : False,
            'display_url': None,
            'orientation':'h'
        }
        file = open(variables_path, 'wb')
        pickle.dump(variables, file)
        file.close()

    driver = webdriver.Chrome(options=options)
    latest_variables = trigger_display(driver=driver, latest_variables=None)

    while True:
        time.sleep(1)
        latest_variables = trigger_display(driver=driver, latest_variables=latest_variables)

if __name__ == '__main__':
    main()


