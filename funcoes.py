import webbrowser, requests, time



def abrir_pagina(url):
    webbrowser.open(url)


def atualizar_item(item_chave, novo_valor):
    payload = {item_chave: novo_valor}    
    try:
        resposta = requests.post("https://pegadinha-ti.vercel.app/pegadinha", json=payload)
        
        if resposta.status_code == 200:
            print(f"{item_chave} atualizado com sucesso para {novo_valor}.")
            print("Resposta do servidor:", resposta.json())
        else:
            print(f"Falha ao atualizar {item_chave}. Status code: {resposta.status_code}")
            print("Resposta:", resposta.text)
    except requests.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")