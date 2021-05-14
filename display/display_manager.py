import subprocess
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options    

class CustomMessageProcessor():

    def __init__(self, data_bytes):
        decoded = data_bytes.decode('utf-8')
        self.message_dict = json.loads(decoded)



    def process(self):
        
        if self.message_dict['type'] == 'display_request':
            
            # change display orientation
            if self.message_dict['orientation'] == 'v':
                orientation = 'right'
            else:
                orientation = 'normal'
            x = subprocess.run(['xrandr', '-o', orientation])

            # connect to site
            print(self.message_dict)

            chrome_options = Options()
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # chrome_options.add_argument("--start-fullscreen");
            chrome_options.add_argument("--kiosk");

            driver = webdriver.Chrome(executable_path=rel('./display/chromedriver'),
                                    chrome_options=chrome_options)
            driver.get('https://www.google.com')
            
            response = 'This worked'.encode(encoding='UTF-8')
            return response

  
chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument("--start-fullscreen");
chrome_options.add_argument("--kiosk");

driver = webdriver.Chrome(executable_path=rel("path/to/chromedriver"),
                          chrome_options=chrome_options)
driver.get('https://www.google.com')