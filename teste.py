from dataclasses import replace
import time
import os
from datetime import datetime

now = datetime.now() # current date and time
inicial =  now.strftime("01%m")
ano =  now.strftime("%Y")
dia = now.strftime("%d")
mes = now.strftime("%m")
ano = str(ano)
ano = ano.replace("20","")

inicial = inicial+ano
fim = dia+mes+ano
nomeArquivo = now.strftime("455-%m-%Y")


print(inicial)
print(fim)
print(nomeArquivo)
