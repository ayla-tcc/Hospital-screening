import serial
import time


porta = "COM7"
velocidade = 9600
arduino2 = serial.Serial(porta, velocidade)

linha2 = str(arduino2.readline())
# print(linha[1:-5])
linha2Split = linha2.split()
print(linha2Split)


def guiBpm():
    # time.sleep(7)
    # while True:

    bpm = float(linha2Split[1].replace('FC=', '').replace(',', ''))
    # print(bpm)
    return bpm


def victorOx():
    # time.sleep(7)

    oxi = float(linha2Split[2].replace('OXI=', '').replace("\\r\\n'", ''))
    return oxi


print(guiBpm())
print(victorOx())
