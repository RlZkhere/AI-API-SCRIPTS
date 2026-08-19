import openai
import os
lista_dati=[]
comando_prompt=''
lista_file=os.listdir()
for file in lista_file:
 if file.startswith('CREA'): #IF FILE IN CURRENT DIRECTORY STARTS WITH CREA THEN THAT'S THE FILE
  file_dati=file
with open(file_dati,'r',encoding='utf-8') as file:
 for riga in file:
  if riga.startswith('SKU'):
   intestazioni=riga.strip().split(';')
  else: 
   lista_dati.append(riga.strip())     
with open('comando.csv','r',encoding='utf-8') as file_comando:
 for riga in file_comando: #SAVE PROMPT
  comando_prompt=comando_prompt+riga
for valore in lista_dati:
 conta=int(0)
 lista_valori=valore.split(';')
 lista_comandi=comando_prompt.split('FINE-COMANDO') #IN THE PROMPT FILE YOU HAVE TO USE A SEPARATOR IF YOU USE CONSECUTIVE PROMPTS
 risultato=''
 for comando in lista_comandi:  
  if conta == 0:
   for x in range(len(intestazioni)):
    valore_vecchio=intestazioni[x] #GET THE POSITION OF THE COLUMN NAME EQUAL TO MARKPLACE IN THE PROMPT 
    valore_nuovo=lista_valori[x] #GET THE ACTUAL VALUE RELATED TO THE MARKPLACE
    comando=comando.replace('"['+valore_vecchio+']"','"'+valore_nuovo+'"') #REPLACE THE MARKPLACE IN THE PROMPT WITH THE ACTUAL VALUE
    #EXAMPLE: IF YOU HAVE "[COLOR]" IN THE PROMPT AND YOU HAVE A CSV FILE WITH A COLUMN NAMED COLOR THAT CONTAINS "GREEN", IN THE PROMPT "COLOR" WILL BE REPLACED WITH "GREEN"
  else:
   if risultato != '':
    comando=comando.replace('"[result]"',"'"+risultato+"'") #IF THE FIRST COMMAND END WITHOUT ERRORS THEN FROM HERE IT WILL WORK USING ALWAYS THE OUTPUT OF THE PROMPT JUST EXECUTED 
   else:
    print('ERROR!!')
    break    
  chiave_api='YOUR_API_KEY'
  client=openai.OpenAI(api_key=chiave_api)
  risposta=client.responses.create(model="gpt-4.1",
                                   instructions="Restituisci esclusivamente la descrizione finale. La descrizione deve essere completa e sviluppata",
                                   input=comando)
  risultato=risposta.output_text
  conta=conta+1
 sku=valore.split(';')[0]
 f=open('OUTPUT/'+str(file_dati),'a')
 f.write(sku+';'+risultato+"\n")
 f.close() 
