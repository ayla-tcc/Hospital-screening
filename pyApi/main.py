from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import asyncio
import mkMd as md
import triF
import time
import serial


app = FastAPI()


def teste(nome: str, cpf: str, resp: str, genre: str, dor: str):
    return (nome, cpf, resp, genre, dor)


@app.get("/")
def home():

    return "API NO AR"


@app.get("/env/{nome}$&{cpf}&{resp}-{genre}-{dor}")
def home(nome, cpf, resp, genre, dor):
    import serialMX as smx
    import serialTemp as stemp

    def ardclose():
        time.sleep(2)
        smx.arduino2.close()
        stemp.arduino.close()
        return 0

    def ardopen():
        time.sleep(3)
        smx.arduino2.open()
        stemp.arduino.open()
        return 0

    if (smx.arduino2.isOpen() == False):
        smx.arduino2.open()

    if (stemp.arduino.isOpen() == False):
        stemp.arduino.open()

    stemp.pedroTemp()
    smx.guiBpm()

    md.dataMed(nome, cpf, resp,
               genre, dor, triF.gravidade(triF.tri(dor, stemp.pedroTemp(), smx.guiBpm(), smx.victorOx())), smx.guiBpm(), smx.victorOx(), stemp.pedroTemp())

    if (smx.arduino2.isOpen() == True):
        smx.arduino2.close()

    if (stemp.arduino.isOpen() == True):
        stemp.arduino.close()

    return RedirectResponse("https://ayla-tcc.github.io/")
