import openai
import os
cartella=os.getcwd()
lista_file=os.listdir(cartella)
file_creazione=''
for x in lista_file:
 if x.startswith('CREA'):
  file_creazione=x
  break     
lista_dati=[]
riga_intestazioni=''
comando=[]
with open(file_creazione,'r',encoding='utf-8') as file:
 for riga in file:
  if riga.startswith('SKU'):
   riga_intestazioni=riga.strip() 
   continue
  with open('comando.csv','r',encoding='utf-8') as file_comando:
   comando_finale=''
   for riga_2 in file_comando:
    riga_nuova=''
    for i,x in enumerate(riga_intestazioni.split(';')):
     sku=riga.split(';')[0]
     if '"['+x+']"' in riga_2:
      valore=riga.split(';')[i]   
      riga_nuova=riga_2.replace('"['+x+']"',valore)
      comando_finale=comando_finale+riga_nuova
    if riga_nuova == '':
     comando_finale=comando_finale+riga_2
  chiave_api='your_api_key'
  client=openai.OpenAI(api_key=chiave_api)  
  risposta=client.responses.create(model="gpt-4.1",      
  instructions="Rispondi con una descrizione abbastanza lunga, adatta ad un e-commerce, codificando il testo in html usando solo il paragrafo <p>, non usare gli a capo",
  input=comando_finale)
  risultato=risposta.output_text  
  if risultato != '':
   f=open('OUTPUT/DESCRIZIONI.csv','a')
   f.write(sku+';'+risultato+"\n")
   f.close()
