from mdutils.mdutils import MdUtils
from mdutils import Html
import markdown
import time
import random
import datetime as dt


def dataMed(nome, cpf, resp, genre, dor, tri_r, Hbpm, Hox, temp):
    anoHoje = dt.datetime.now().year
    datenow = dt.datetime.now()

    hox = Hox
    Stemp = temp
    hbpm = Hbpm
    tri_result = tri_r
    pnum_var = random.randrange(1000)
    nomep_var = nome
    respNome_var = resp
    genero_var = genre
    tDor_var = dor
    cpf_var = cpf

    # -------------------------------------
    mdFile = MdUtils(file_name='P{pnum}'.format(
        pnum=pnum_var))

    mdFile.new_line("# Paciente numero: {pnum}".format(pnum=pnum_var))
    mdFile.new_line(
        "### Resultado Triagem - Gravidade/risco: {tri}".format(tri=tri_result))
    mdFile.new_line("### Data: {datanow}".format(datanow=datenow))
    mdFile.create_md_file()

    mdFile.new_line("---")

    mdFile.new_line("### Nome: {nome}"
                    .format(nome=nomep_var))
    mdFile.new_line("### Genero: {genero}".format(genero=genero_var))
    mdFile.new_line("### Local da dor: {dor}".format(dor=tDor_var))

    mdFile.new_line("---")
    mdFile.new_line(" ")
    mdFile.new_line("CPF: {cpf}".format(cpf=cpf_var))
    mdFile.new_line("Nome-Responsavel: {respNome}".format(
        respNome=respNome_var))
    mdFile.new_line(" ")
    mdFile.new_line("---")
    mdFile.new_line("### Sensores:")
    mdFile.new_line("### BPM:{bpm} | OX:{ox}%  | TEMP:{t}℃".format(
        bpm=hbpm, ox=hox, t=Stemp))
    mdFile.create_md_file()


# def teste():
#     mdFile = MdUtils(file_name='paciente{pnum}'.format(
#         pnum=pnum_var), title='paciente{pnum}'.format(pnum=pnum_var))

#     mdFile.new_line("### Nome: {nome}".format(nome=nomep_var))

#     mdFile.new_line("### Idade: {idade}".format(idade=idadep_var))

#     while True:
#         time.sleep(1)
#         mdFile.new_line("### Sensor Batimento: {dados}".format(
#             dados=comSerial.ttrue()))
#         mdFile.create_md_file()


# markdown.markdownFromFile(input='paciente{pnum}.md'.format(
#     pnum=pnum_var), output='paciente{pnum}.html'.format(
#     pnum=pnum_var))
