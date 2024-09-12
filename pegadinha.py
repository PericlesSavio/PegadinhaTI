import requests, json, time
from funcoes import abrir_pagina, atualizar_item
from playsound import playsound
#pyinstaller --onefile main.py

while True:
	url = "https://pegadinha-ti.vercel.app/pegadinha"
	response = requests.request("GET", url)
	saida = json.loads(response.text)
    
	if saida.get('item1') == False:
		print('Falso')
		time.sleep(2)
	elif saida.get('item1') == True:
		print('True')
		# abrir_pagina('google.com.br')
		atualizar_item('item1', False)
		playsound('./mp3.mp3')
		time.sleep(2)

