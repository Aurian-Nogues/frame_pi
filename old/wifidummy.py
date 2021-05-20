from blufi import AbstractWiFiHandler

class WiFiHandler(AbstractWiFiHandler):
    def InitiateScan(self):
        print('inititate Wifi SCAN in the background')
        #this function must be asynchronous (nonblocking)

    def CheckScanResult(self):
        """Check whether WiFi scan finished and return the result"""
        self.scantries += 1
        if self.scantries == 8: #this check is only for simulation of WiFi scan behavior
            self.scantries = 0
            print('Wifi SCAN completed')
            #artificial scan result
            resp = [{'SSID':b'SSID #1', 'RSSI':-32}, 
                    {'SSID':b'SSID # 2 xyz\x80', 'RSSI':-32}
                    ]
            for i in range(0,10):
                resp.append({'SSID':b'SSID TEST #%d' % i, 'RSSI':-23})
            return resp
            
            #empty list can be returned
            return []

        #no result available yet
        return None

    def Connect(self):
        #connect requested
        print('CONNECT to AP', self.config)

    def GetWifiStatus(self):
        print('WIFI STATUS requested')
        activeSSID, isConnected = b'activeSSID', True
        return activeSSID, isConnected

