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
options.add_argument("--noerrdialogs")
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches" , ["enable-automation"])
options.add_experimental_option("excludeSwitches" , ["enable-automation","load-extension"])
options.add_experimental_option('useAutomationExtension', False)

#BASE_DIR = os.getcwd()
BASE_DIR =  "/home/pi/frame_pi"
DISPLAY_DIR = os.path.join(BASE_DIR, 'display')
PAGES_DIR = os.path.join(BASE_DIR, 'display', 'pages')
variables_path = os.path.join(DISPLAY_DIR, 'variables')
wait_page_path = os.path.join(PAGES_DIR, 'waiting_page.html')
no_wifi_url = os.path.join(PAGES_DIR, 'no_wifi.html')

WIFI_CONNECTION_TRIES = 10

import socket

def isConnected():

    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
            WIFI_CONNECTION_TRIES = 0
        return True
    except OSError:
        WIFI_CONNECTION_TRIES = WIFI_CONNECTION_TRIES -1
    return False


def trigger_display(driver, latest_variables):
    file = open(variables_path, 'rb')
    variables = pickle.load(file)
    file.close()

    if variables['wifi_connected'] == False:
        if WIFI_CONNECTION_TRIES > 0:
            connected = isConnected()
            # the frame connected, update values
            variables['wifi_connected'] = connected
            file = open(variables_path, 'wb')
            pickle.dump(variables, file)
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

        connected = isConnected()
        # create default variables file
        # /!\/!\ Do not use that for startup run. This will work in dev but when in prod the script needs a variables file at start or it will crash /!\/!\
        print('Variables file does not exit, creating it')
        variables = {
            'wait_url': 'file://' + wait_page_path, # need this prefix when loading from local drive
            'no_wifi_url' : 'file://' + no_wifi_url,
            'wifi_connected' : connected,
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
        print

if __name__ == '__main__':
    main()


