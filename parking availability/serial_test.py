import serial
import time

data = serial.Serial(
                  'COM5',
                  baudrate = 9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,                  
                  timeout=1
                  )

def read_data():
    print('reading.....')
    Data = []
    while True:
        data.write(str.encode('O'))
        time.sleep(1)
        d = data.readline()
        d = d.decode('UTF-8', 'ignore')
        if d:
            d = d.split(',')
            print(d)
            if len(d) == 3:
                Data.append(int(d[0]))
                Data.append(int(d[1]))
                Data.append(int(d[2].replace('\r\n', '')))
                break
    return Data