import serial
import time

porta = "COM3"
velocidade = 9600

arduino = serial.Serial(porta, velocidade)


def teste(opcao):
    while True:

        if opcao == 'A':
            arduino.write(b'A')

            linha = str(arduino.readline())
            print(linha[1:-5])
            time.sleep(1.8)
