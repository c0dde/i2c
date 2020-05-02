dimport time
import smbus
import sys

bus = smbus.SMBus(1) #connect to IC2-bus

#Arduino address
address_arduino=0x8

try:
    
    while True:
        
        my_data=bus.read_byte(address_arduino)

        if my_data < 20:
            print(my_data, "Too dark")
        elif my_data < 40:
            print(my_data, "Dark")
        elif my_data < 60:
            print(my_data, "Medium")
        elif my_data < 80:
            print(my_data, "Bright")
        else:
            print(my_data, "Too Bright")

        time.sleep(1)
except KeyboardInterrupt:
    pass