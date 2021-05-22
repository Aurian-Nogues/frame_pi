import logging, time, os
import dbus
from bluezero import adapter
from blufi import BluFi, AbstractWiFiHandler
from blufi.agent import AgentDisplayOnly, Agent, AgentNoDisplayNoKeyboard, install_agent
from wifinm import WiFiHandlerNetworkManager
import json

from display.display_trigger import DisplayTrigger

# test
DEVICE_NAME = "BLUFI_DEVICE"
PAIRING_ENABLED = False #supported reliably only by iOS devices

def main(adapter_address):
    """Creation of peripheral"""
    logger = logging.getLogger('localGATT')
    logger.setLevel(logging.DEBUG)

    # Create peripheral
    dev = BluFi(WiFiHandlerNetworkManager, adapter_address, DEVICE_NAME)

    trigger = DisplayTrigger()
    ssid, connected = dev.wifi.GetWifiStatus()

    response = trigger.trigger_display(wifi_connected=connected)

    def on_customdata(data):
        decoded = data.decode('utf-8')
        message_dict = json.loads(decoded)
        if message_dict['type'] == 'display_request':
            # {'type': 'display_request',
            #  'orientation': 'v',
            #   'url': 'https://frame-zero.herokuapp.com/player/4/0x60F80121C31A0d46B5279700f9DF786054aa5eE5/913180/v/57%25/auto/%23000000'}
            url = message_dict['url']
            orientation = message_dict['orientation']

        trigger = DisplayTrigger()
        ssid, connected = dev.wifi.GetWifiStatus()
        response = trigger.trigger_display(display_url=url, orientation=orientation, wifi_connected=connected)
        response = json.dumps(response)
        dev.send_custom_data(bytes(response, encoding='utf8'))

        # dev.send_custom_data(response)
        # print('CUSTOM data received', data)
        # dev.send_custom_data(b'xyz')

    dev.on_customdata = on_customdata
    # Publish peripheral and start event loop
    dev.publish()

# class MyAgent(AgentDisplayOnly): #device with Display capability (no Keyboard input possible)
#     def on_passkey(self, passkey):
#         print('Display passkey on the screen:', passkey)
        
if __name__ == '__main__':
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

    if 0:
       os.system("killall wpa_supplicant")
       os.system("systemctl stop wpa_supplicant") 
       os.system("systemctl restart NetworkManager")

    os.system("bluetoothctl paired-devices") #can be removed, it is just for showing paired devices in case of any issue with failing connection of remote Bluetooth devices
    os.system("/etc/init.d/bluetooth restart") #can be removed, it is just for ensuring the clean initial state

    time.sleep(1)
    adapter = list(adapter.Adapter.available())
    if len(adapter):
        adapter = adapter[0]
        adapter.powered = dbus.Boolean(False)
        time.sleep(.5)
        adapter.powered = dbus.Boolean(True)
        adapter.alias=DEVICE_NAME

        #print(adapter.alias, adapter.powered, adapter.pairable, adapter.pairabletimeout)
        if PAIRING_ENABLED:
                #Enable pairing
                adapter.pairable = dbus.Boolean(True) #Switches an adapter to pairable or non-pairable mode.
                #install_agent(MyAgent, adapter)
                install_agent(AgentNoDisplayNoKeyboard, adapter)
                
        else:
                #Disable pairing
                adapter.pairable = dbus.Boolean(False) #Switches an adapter to pairable or non-pairable mode.
                install_agent(AgentNoDisplayNoKeyboard, adapter) 

        #print(adapter.alias, adapter.powered, adapter.pairable, adapter.pairabletimeout)
        main(adapter.address)
    else:
        print("No BLE adapter found")
