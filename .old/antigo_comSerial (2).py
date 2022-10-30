import serial

porta = "COM4"
velocidade = 9600

arduino = serial.Serial(porta, velocidade);


def sensores(opcao):
    while True:

        if opcao == 'A':
            arduino.write(b'A')

        linha = str(arduino.readline())
        print(linha[1:-5])


arduino.close()