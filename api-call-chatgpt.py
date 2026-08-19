import openai
import os
lista_file=os.listdir()
for file in lista_file:
 if file.startswith('TITOLI'): #LIST THE DIRECTORY, IF FILE STARTS WITH TITOLI THEN IT WILL USE IT 
  file_traduci=file     
lista_titoli=[]
comando_istruzioni=''
lingue=['inglese','francese','tedesco','spagnolo'] #LANGUAGES THAT IT WILL USE
correlazioni={'inglese':'UK','francese':'FR','tedesco':'DE','spagnolo':'ES'} #CORRELATION BETWEEN LANGUAGE AND EXTENSION
with open(file_traduci,encoding='utf-8') as file_dati:
 for riga in file_dati:
  lista_titoli.append(riga.strip())
chiave_api='YOUR_API-KEY'
client=openai.OpenAI(api_key='YOUR_API-KEY')
for valore in lista_titoli:
 titolo_traduci=valore.split(';')[1]
 sku=valore.split(';')[0] 
 for lingua in lingue:
  comando_istruzioni='Traduci in '+lingua+': '+titolo_traduci+',fornisci come output solo il testo tradotto.'
  risposta=client.responses.create(model="gpt-4.1",
  instructions="Rispondi esclusivamente con il testo tradotto, senza spiegazioni.",
  input=comando_istruzioni
  )
  risultato=risposta.output_text
  estensione=correlazioni[lingua]
  if risultato != '':
   f=open('OUTPUT/'+file_traduci.replace('.csv','')+'-'+estensione+'.csv','a')
   f.write(sku+';'+risultato+"\n")
   f.close()   
