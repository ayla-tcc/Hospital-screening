import serial
import time


porta = "COM3"
velocidade = 9600
arduino2 = serial.Serial(porta, velocidade)



def guiBpm():
    # time.sleep(7)
    # while True:
    linha2 = str(arduino2.readline())
    # print(linha[1:-5])
    linha2Split = linha2.split()
    bpm = float(linha2Split[1].replace('FC=', '').replace(',', ''))
    # print(bpm)
    return bpm


def victorOx():
    # time.sleep(7)
    linha2 = str(arduino2.readline())
    # print(linha[1:-5])
    linha2Split = linha2.split()
    oxi = float(linha2Split[2].replace('OXI=', '').replace("\\r\\n'", ''))
    print(linha2Split)
    return oxi



print(guiBpm())
print(victorOx())
