#Exercício Python 114: Crie um código em Python que teste se o site pudim está
# acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site pudim está inacessível')
else:
    print('Parabéns você pode acessar o site do pudim')