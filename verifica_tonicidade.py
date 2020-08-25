# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 02:54:26 2020

@author: brian
"""

#!/usr/bin/python
import MySQLdb

#CONECTANDO COM O BANCO
con = MySQLdb.connect(host="localhost", user="root", passwd="", db="dicionario_portugues")
con.select_db('dicionario_portugues')

#CONSULTANDO DADOS NAS TABELAS
cursor = con.cursor()
cursor.execute("SELECT palavra, id_palavra FROM dicionario")# Executa a consulta na tabela selecionada
con.commit()
for row in cursor.fetchall():
    palavra = row[0]
    contador = 0
    tem_acento = 0
    for i in range(0,len(palavra)):
        if((ord(palavra[i]) == 224) or (ord(palavra[i]) == 225) or (ord(palavra[i]) == 226) or (ord(palavra[i]) == 227) 
        or (ord(palavra[i]) == 228) or (ord(palavra[i]) == 229)
        or (ord(palavra[i]) == 232) or (ord(palavra[i]) == 233) or (ord(palavra[i]) == 234) or (ord(palavra[i]) == 235)
        or (ord(palavra[i]) == 236) or (ord(palavra[i]) == 237) or (ord(palavra[i]) == 238) or (ord(palavra[i]) == 239)
        or (ord(palavra[i]) == 242) or (ord(palavra[i]) == 243) or (ord(palavra[i]) == 244) or (ord(palavra[i]) == 245)
        or (ord(palavra[i]) == 246) or (ord(palavra[i]) == 249) or (ord(palavra[i]) == 250) or (ord(palavra[i]) == 251)
        or (ord(palavra[i]) == 252)):
            tem_acento = 1
        if(ord(palavra[i]) == 183 and tem_acento == 1):
            contador = contador + 1
    if(contador == 1):
        cursor.connection.autocommit(True)
        cursor.execute("UPDATE dicionario SET tonicidade = 2 WHERE dicionario.id_palavra = "+str(row[1])+" ")
    if(contador == 2):
        cursor.connection.autocommit(True)
        cursor.execute("UPDATE dicionario SET tonicidade = 3 WHERE dicionario.id_palavra = "+str(row[1])+" ")
    if(contador == 0):
        cursor.connection.autocommit(True)
        cursor.execute("UPDATE dicionario SET tonicidade = 1 WHERE dicionario.id_palavra = "+str(row[1])+" ")

cursor.close()
con.close()

# =============================================================================
# if((ord(palavra[len(palavra)-1]) == 114) or (ord(palavra[len(palavra)-1]) == 122) or (ord(palavra[len(palavra)-1] == 108) or
#         ord(palavra[len(palavra)-1]) == 120) or ord(palavra[len(palavra)-1]) == 105) or ord(palavra[len(palavra)-1]) == 117)):
# =============================================================================
