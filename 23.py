import pyshark

cap = pyshark.FileCapture('C:/Users/hasan/Desktop/wsh.pcapng')
print(cap[50])