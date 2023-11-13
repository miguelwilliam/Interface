import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}
    '''

    texto_moedas['text'] = texto



janela = Tk()
janela.title('COTAÇÃO ATUAL DAS MOEDAS')
texto_orientacao = Label(janela, text='Clique no botão para exibir a cotação atual das moedas.')
texto_orientacao.grid(row=0, column=0, padx=20, pady=20)
botao_exibir = Button(janela, text='EXIBIR', command=pegar_cotacoes)
botao_exibir.grid(row=1, column=0, pady=20)
texto_moedas = Label(janela, text='')
texto_moedas.grid(row=2, column=0)


janela.mainloop()