# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:53:46 2020

@author: brian
"""

#!/usr/bin/python
import MySQLdb
from urllib.request import urlopen
from bs4 import BeautifulSoup

#CONECTANDO COM O BANCO
con = MySQLdb.connect(host="localhost", user="root", passwd="", db="dicionario_portugues")
con.select_db('dicionario_portugues')

#CRIANDO UMA LISTA COM O ALFABETO PARA NAVEGAR PELAS URLS DO SITE
alfabeto = []
for i in range(ord('a'), ord('z')+1):
    alfabeto.append(chr(i))

for letra in alfabeto:
    response = urlopen('http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter='+ str(letra)+'&start=0')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')
    soup = soup.find('td', {'id': 'maintext'})
    soup = soup.findAll('p')
    npaginas = int(soup[2].getText().split()[-3])
    print("Coletando ", npaginas, " palavras que começam com ", letra)
    
    for i in range(0,npaginas,20):
        response = urlopen('http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter='+ str(letra)+'&start=' + str(i))
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        soup = soup.find('td',{'title': 'Palavra'})
        infos = soup.findAll('a')
        
        cont = 0
        for info in infos:
            if cont%2==0:
                #INSERINDO PALAVRAS NA TABELA
                cursor = con.cursor()
                cursor.connection.autocommit(True)
                sql="INSERT INTO dicionario(palavra) VALUES ('"+str(info.getText())+"')"
                cursor.execute(sql)
                cursor.close()
            cont = cont+1
    
con.close()