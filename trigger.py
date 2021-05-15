import pickle
import subprocess
import os
import time

BASE_DIR = os.getcwd()
DISPLAY_DIR = os.path.join(BASE_DIR, 'display')
INTERPRETER = os.path.join(BASE_DIR, 'venv', 'bin', 'python3')

display_manager = os.path.join(DISPLAY_DIR,'test_manager.py')
variables_file = os.path.join(DISPLAY_DIR, 'variables')




# x = subprocess.run([INTERPRETER, display_manager])

time.sleep(5)
print('nft')
variables = {
    'wait_url': 'https://www.google.com',
    'display_url': 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/h/auto/100%25/%23000000'
}
file = open(variables_file, 'wb')
pickle.dump(variables, file)
file.close()


time.sleep(5)
print('google')
variables = {
    'wait_url': 'https://www.google.com',
    'display_url': None
}
file = open(variables_file, 'wb')
pickle.dump(variables, file)
file.close()


time.sleep(5)
print('nft')
variables = {
    'wait_url': 'https://www.google.com',
    'display_url': 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/h/auto/100%25/%23000000'
}
file = open(variables_file, 'wb')
pickle.dump(variables, file)
file.close()
# 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/h/auto/100%25/%23000000'

