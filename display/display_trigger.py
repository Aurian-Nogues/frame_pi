import os
import pickle


class DisplayTrigger():

    def __init__(self):
        self.BASE_DIR = os.getcwd()
        self.DISPLAY_DIR = os.path.join(self.BASE_DIR, 'display')
        self.display_manager = os.path.join(self.DISPLAY_DIR,'test_manager.py')
        self.variables_file = os.path.join(self.DISPLAY_DIR, 'variables')
    
    def trigger_display(self, url):
        variables = {
            'wait_url': 'https://www.google.com',
            'display_url': url
        }
        file = open(self.variables_file, 'wb')
        pickle.dump(variables, file)
        file.close()