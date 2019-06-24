#---------------------------------------#
# Desenvolvedor: Fabio Eduardo do Vale  #
# Data: 13/06/2019                      #
# Versão: 0.0.1                         #
#---------------------------------------#
from gtts import gTTS
from datetime import datetime
import os
import random

minuto_atual = None

lista_nome = ['Alan Turing', 
              'Ada lovelace',
              'Tim Berners-Lee',
              'Donald Knuth',
              'Fabio do Vale',
              'Grace Hopper',
              'Guido van Rossum',
              'Bjarne Stroustrup',
              'Dennis Ritchie',
            ]

while True:
    data_atual  = datetime.now()
    hora        = data_atual.hour
    minuto      = data_atual.minute
    segundos    = data_atual.second

    #if(minuto_atual != minuto):
    if(1 == 1):
        nome_sorteado = random.choice(lista_nome)
        minuto_atual = minuto
        print(str(hora)+":"+str(minuto)+":"+str(segundos))
        frase = nome_sorteado + ", agora são: " + str(hora) + "horas e " + str(minuto) + "minutos"
        tts = gTTS(text = frase, lang='pt')
        tts.save('frase.mp3')

        os.system('mpg123 frase.mp3')


