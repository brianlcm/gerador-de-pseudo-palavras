# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:51:42 2020

@author: brian
"""

#!/usr/bin/python
import MySQLdb

#CONECTANDO COM O BANCO
con = MySQLdb.connect(host="localhost", user="root", passwd="", db="dicionario_portugues")
con.select_db('dicionario_portugues')

verifica = 1

#CONSULTANDO DADOS NAS TABELAS
cursor = con.cursor()
cursor.execute("SELECT palavra, id_palavra FROM dicionario")# Executa a consulta na tabela selecionada
con.commit()
for row in cursor.fetchall():
    palavra = row[0]
    if(len(palavra)>2):
        if ord(palavra[len(palavra)-2])==183:
            verifica = 0
        else:
            for i in range(2,len(palavra),3):
                if(ord(palavra[i]) == 183):
                    
                    if ((ord(palavra[i-1]) == 97) or (ord(palavra[i-1]) == 101) or (ord(palavra[i-1]) == 225) or (ord(palavra[i-1]) == 105)
                    or (ord(palavra[i-1]) == 111) or (ord(palavra[i-1]) == 117) or (ord(palavra[i-1]) == 224) or (ord(palavra[i-1]) == 225)
                    or (ord(palavra[i-1]) == 226) or (ord(palavra[i-1]) == 227) or (ord(palavra[i-1]) == 228) or (ord(palavra[i-1]) == 229)
                    or (ord(palavra[i-1]) == 232) or (ord(palavra[i-1]) == 233) or (ord(palavra[i-1]) == 234) or (ord(palavra[i-1]) == 235)
                    or (ord(palavra[i-1]) == 236) or (ord(palavra[i-1]) == 237) or (ord(palavra[i-1]) == 238) or (ord(palavra[i-1]) == 239)
                    or (ord(palavra[i-1]) == 242) or (ord(palavra[i-1]) == 243) or (ord(palavra[i-1]) == 244) or (ord(palavra[i-1]) == 245)
                    or (ord(palavra[i-1]) == 246) or (ord(palavra[i-1]) == 249) or (ord(palavra[i-1]) == 250) or (ord(palavra[i-1]) == 251)
                    or (ord(palavra[i-1]) == 252)):
                        verifica = 1
                        
                        if ((ord(palavra[i-2]) != 97) and (ord(palavra[i-2]) != 101) and (ord(palavra[i-2]) != 225) and (ord(palavra[i-2]) != 105)
                        and (ord(palavra[i-2]) != 111) and (ord(palavra[i-2]) != 117) and (ord(palavra[i-2]) != 224) and (ord(palavra[i-2]) != 225)
                        and (ord(palavra[i-2]) != 226) and (ord(palavra[i-2]) != 227) and (ord(palavra[i-2]) != 228) and (ord(palavra[i-2]) != 229)
                        and (ord(palavra[i-2]) != 232) and (ord(palavra[i-2]) != 233) and (ord(palavra[i-2]) != 234) and (ord(palavra[i-2]) != 235)
                        and (ord(palavra[i-2]) != 236) and (ord(palavra[i-2]) != 237) and (ord(palavra[i-2]) != 238) and (ord(palavra[i-2]) != 239)
                        and (ord(palavra[i-2]) != 242) and (ord(palavra[i-2]) != 243) and (ord(palavra[i-2]) != 244) and (ord(palavra[i-2]) != 245)
                        and (ord(palavra[i-2]) != 246) and (ord(palavra[i-2]) != 249) and (ord(palavra[i-2]) != 250) and (ord(palavra[i-2]) != 251)
                        and (ord(palavra[i-2]) != 252)):
                            verifica = 1
                            
                        else:
                            verifica = 0
                            break
                    else:
                        verifica = 0
                        break
                else:
                    verifica = 0
                    break
    else:
          
        if(len(palavra)==1):
            verifica = 0
        else:
            if ((ord(palavra[1]) == 97) or (ord(palavra[1]) == 101) or (ord(palavra[1]) == 225) or (ord(palavra[1]) == 105)
            or (ord(palavra[1]) == 111) or (ord(palavra[1]) == 117) or (ord(palavra[1]) == 224) or (ord(palavra[1]) == 225)
            or (ord(palavra[1]) == 226) or (ord(palavra[1]) == 227) or (ord(palavra[1]) == 228) or (ord(palavra[1]) == 229)
            or (ord(palavra[1]) == 232) or (ord(palavra[1]) == 233) or (ord(palavra[1]) == 234) or (ord(palavra[1]) == 235)
            or (ord(palavra[1]) == 236) or (ord(palavra[1]) == 237) or (ord(palavra[1]) == 238) or (ord(palavra[1]) == 239)
            or (ord(palavra[1]) == 242) or (ord(palavra[1]) == 243) or (ord(palavra[1]) == 244) or (ord(palavra[1]) == 245)
            or (ord(palavra[1]) == 246) or (ord(palavra[1]) == 249) or (ord(palavra[1]) == 250) or (ord(palavra[1]) == 251)
            or (ord(palavra[1]) == 252)):
                verifica = 1
                if ((ord(palavra[0]) != 97) and (ord(palavra[0]) != 101) and (ord(palavra[0]) != 225) and (ord(palavra[0]) != 105)
                and (ord(palavra[0]) != 111) and (ord(palavra[0]) != 117) and (ord(palavra[0]) != 224) and (ord(palavra[0]) != 225)
                and (ord(palavra[0]) != 226) and (ord(palavra[0]) != 227) and (ord(palavra[0]) != 228) and (ord(palavra[0]) != 229)
                and (ord(palavra[0]) != 232) and (ord(palavra[0]) != 233) and (ord(palavra[0]) != 234) and (ord(palavra[0]) != 235)
                and (ord(palavra[0]) != 236) and (ord(palavra[0]) != 237) and (ord(palavra[0]) != 238) and (ord(palavra[0]) != 239)
                and (ord(palavra[0]) != 242) and (ord(palavra[0]) != 243) and (ord(palavra[0]) != 244) and (ord(palavra[0]) != 245)
                and (ord(palavra[0]) != 246) and (ord(palavra[0]) != 249) and (ord(palavra[0]) != 250) and (ord(palavra[0]) != 251)
                and (ord(palavra[0]) != 252)):
                    verifica = 1
                else:
                    verifica = 0
                                    
            else:
                verifica = 0
        
    if(verifica==1):
        cursor.connection.autocommit(True)
        cursor.execute("UPDATE dicionario SET canonicidade = 1 WHERE dicionario.id_palavra = "+str(row[1])+" ")
    else:
        cursor.connection.autocommit(True)
        cursor.execute("UPDATE dicionario SET canonicidade = 0 WHERE dicionario.id_palavra = "+str(row[1])+" ")

cursor.close()
con.close()