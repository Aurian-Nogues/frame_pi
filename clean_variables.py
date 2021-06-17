import pickle
import os

BASE_DIR =  "/home/pi/frame_pi"
DISPLAY_DIR = os.path.join(BASE_DIR, 'display')
PAGES_DIR = os.path.join(BASE_DIR, 'display', 'pages')
variables_path = os.path.join(DISPLAY_DIR, 'variables')
wait_page_path = os.path.join(PAGES_DIR, 'waiting_page.html')
no_wifi_url = os.path.join(PAGES_DIR, 'no_wifi.html')

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