
import serial
import time

porta = "COM3"
velocidade = 9600

arduino = serial.Serial(porta, velocidade)


def pedroTemp():
    while True:
        time.sleep(7)
        linha = str(arduino.readline())
        # print(linha[1:-5])
        linhaSplit = linha.split()
        time.sleep(1.8)
        temp = float(linhaSplit[0].replace("b'", '').replace("\\r\\n'", ''))
        # print(temp)
        # print('-----------------------')
        # print(linhaSplit)
        break
    return temp


print(pedroTemp())
