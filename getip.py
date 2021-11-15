import tinytuya

def ip(deviceID):
    devices = tinytuya.deviceScan(verbose=False,maxretry= 1,poll = False)
    for i in devices:
        if devices[i]['gwId'] == deviceID:
            print(devices[i]['ip'])
            return devices[i]['ip']