import nmcli

#nmcli.radio.wifi_off()

if not nmcli.radio.wifi():
    #Turn on Wi-Fi radio switches.
    nmcli.radio.wifi_on()

IFC = 'wlan0'
#rescan
nmcli.device.wifi_rescan(ifname=IFC)

for ap in nmcli.device.wifi():
    print(ap)
