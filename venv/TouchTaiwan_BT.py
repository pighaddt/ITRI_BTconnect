import bluetooth

###
target_name = "LAIRD BL654-CD8A74"
target_address = "f00f06cd8a74" # Touch Taiwan Device ()

nearby_devices = bluetooth.discover_devices()
print(nearby_devices)
print()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print("Found target bluetooth device with address: ", target_address)
else:
    print("Could not find target bluetooth device nearby")


##
import serial

portx = "COM4"
bps = 9600

A = []
ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE, stopbits=1)
if (ser.isOpen()):
    print("open success")
    while (True):
        line = ser.readline()
        # if(line):
        #     a = str(line, 'utf-16')
        #     print(a)
        #     line = 0

else:
    print("open failed")

ser.close()



