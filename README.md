# DESCRIPTION

This app is for WiFi provisioning over Bluetooth.

# PREREQUISITES

The app uses Network manager to configure the WiFi.

## Install packages

    sudo apt update
    sudo apt install network-manager

## Configure dhcpcd to ignore wlan0

To avoid issues with duplicate instances of wpa_supplicant preventing NetworkManager to work properly, we need to modify the default settings. If we kept the setting as is, the wpa_supplicant will be called twice. The first instance will be called by the wpa_supplicant.service, the second one will be executed by dhcpcd deamon. 

To mitigate this issue, first check `/etc/network/interfaces`; this should be empty except for an include from `/etc/network/interfaces.d` (which is in turn empty). This is valid when we have a fresh install of Raspbian.

Then edit `/etc/dhcpcd.conf`, add line:

    denyinterfaces wlan0

This disables execution of the duplicate wpa_supplicant instance.

Then configure Network Manager to control wlan0 and assume dhcp duties. Edit `/etc/NetworkManager/NetworkManager.conf`:

    [main]
    plugins=ifupdown,keyfile
    dhcp=internal
    
    [ifupdown]
    managed=true

Finaly, restart the raspberry to take the modifications into effect.

`sudo reboot`

Make sure that there is only one wpa_supplicant instance running after reboot

`ps axu | grep supplicant`




# PYTHON part

Python uses Bluez library via bluezero (DBUS)

# PREREQUISITES
Bluez
Python 3.7+

The mandatory Python packages:
```
$ sudo pip3 install dbus-python
$ sudo pip3 install bluezero
```

# EXAMPLE

Direct usage

```console
$ sudo python3.7 main.py
$ sudo python3 main.py
```

Python virtual environment

```
$ sudo apt install libgirepository1.0-dev
$ sudo apt install libcairo2-dev

$ python3.7 -m venv ble-env
$ source ble-env/bin/activate
(ble-env) $ pip3 install dbus-python
(ble-env) $ pip3 install PyGObject
(ble-env) $ pip3 install bluezero
(ble-env) $ pip3 install bisturi
(ble-env) $ pip3 install uptime
(ble-env) $ pip3 install python-networkmanager
(ble-env) $ sudo ble-env/bin/python3.7 main.py
```

# DISPLAY
# chromium drivers recommended by selenium will not work on ARM chips. Use this command to install the right ARM drivers
sudo apt install chromium-chromedriver
$ pip3 install selenium

