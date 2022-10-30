def tri(dor, temp, fc, oxi):

    def riscoD():
        riscoDor = 0
        if (dor == 'cabeca'):
            riscoDor = 1
        elif (dor == 'peito'):
            riscoDor = 2
        elif (dor == 'barriga'):
            riscoDor = 0
        print('RiscoDor = ', riscoDor)
        return riscoDor

    def riscoT():
        riscoTemp = 0
        if (temp >= 34 and temp >= 36 and temp < 37.5):
            riscoTemp = 0
        elif (temp >= 37.5 and temp <= 39):
            riscoTemp += 2
        elif (temp > 39 or temp < 34):
            riscoTemp += 3
        print('RiscoTemp = ', riscoTemp)
        return riscoTemp

    def riscoH():
        riscoFc = 0
        if (fc >= 100 and fc <= 120):
            riscoFc += 1
        elif (fc > 120 and fc <= 140):
            riscoFc += 2
        elif (fc > 140 or fc < 80):
            riscoFc += 3
        print('RiscoFc = ', riscoFc)
        return riscoFc

    def riscoOx():
        riscooxi = 0
        if (oxi >= 90):
            riscooxi = 0
        elif (oxi <= 89):
            riscooxi += 1
        print('RiscoOxi = ', riscooxi)
        return riscooxi

    riscoTotal = riscoD() + riscoT() + riscoH() + riscoOx()
    print('RiscoTotal = ', riscoTotal)
    return riscoTotal

# print(tri('cabeca',20,150))
#  (Amarela - (Media) )


def gravidade(trig):
    if (trig == 9 or trig == 10):
        return '(Vermelha - (Muito Alta))'
    elif (trig == 8 or trig == 7):
        return '(Laranja - (Alta))'
    elif (trig == 6 or trig == 5):
        return '(Amarela - (Media))'
    elif (trig == 4 or trig <= 3):
        return '(Verde - (Baixa))'
