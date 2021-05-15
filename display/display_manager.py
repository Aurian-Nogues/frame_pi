import subprocess
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import os  



class CustomMessageProcessor():

    def __init__(self, data_bytes):
        decoded = data_bytes.decode('utf-8')
        self.message_dict = json.loads(decoded)

    def process(self):
        
        if self.message_dict['type'] == 'display_request':
            
            # # change display orientation
            # if self.message_dict['orientation'] == 'v':
            #     orientation = 'right'
            # else:
            #     orientation = 'normal'
            # x = subprocess.run(['xrandr', '-o', orientation])

            # connect to site
            url = self.message_dict['url']
            print('=========================')
            print(url)
            print('=========================')
            

            chrome_options = Options()
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_argument("--start-fullscreen");
            chrome_options.add_argument("--kiosk")

            driver_path = os.path.join(os.getcwd(), 'display', 'chromedriver')

            driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
            driver.get(url)
            
            response = 'This worked'.encode(encoding='UTF-8')
            return response
