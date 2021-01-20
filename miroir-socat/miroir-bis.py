import serial

ser = serial.Serial(
        port='/dev/pts/13',
        baudrate = 2400,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
)

while 1:
        if(ser.in_waiting > 5000000):
                x = ser.readline()
                #ser.write(x)

                print("Port série: ", x.decode())

