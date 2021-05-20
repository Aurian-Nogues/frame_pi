import dbus
from dbus.exceptions import DBusException
import NetworkManager
import os
#import psutil
import datetime, time

from uptime import uptime, boottime

#print(boottime())
#print(uptime())


from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

for c in NetworkManager.Settings.ListConnections():
    print(c.GetSettings(), c.Filename)

#Display all visible SSIDs
for dev in NetworkManager.NetworkManager.GetDevices():
    if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
        continue


    print(dev.State)
    dev = dev.SpecificDevice()
    #os.system("nmcli dev")
    print(dev.State, dev.StateReason)
    #viz https://developer.gnome.org/NetworkManager/stable/nm-dbus-types.html#NMDeviceState
    
    print('lastscan',dev.LastScan, uptime()  - dev.LastScan/1000.0) #The timestamp (in CLOCK_BOOTTIME milliseconds) for the last finished network scan. A value of -1 means the device never scanned for access points.


    #print(dir(dev))

    if uptime() - dev.LastScan/1000.0 > 30:
        try:
            dev.RequestScan(options=dict())
            #os.system("nmcli dev")
            time.sleep(5)
        except Exception as e:
            print('Scan failed', e)
            pass


    active = dev.ActiveAccessPoint
    aps = dev.GetAllAccessPoints()
    for ap in aps:
            prefix = '* ' if ap.object_path == active.object_path else '  '
            print("%s %s  %s lastseen:%d, mode:%d, rssi:%d, wpaf:%d" % (prefix, ap.Ssid, ap.HwAddress, ap.LastSeen, ap.Mode, ap.Strength, ap.WpaFlags))  


#        ssid_configs = device.GetAccessPoints()
#        # rescan if only finds 1 (the connected one) or less APs
#        if len(ssid_configs) <= 1:
#            # rescan ssid
#            device.RequestScan(options=dict())

    #for ap in dev.GetAccessPoints():
    #    print('%-30s %dMHz %d%%' % (ap.Ssid, ap.Frequency, ap.Strength))