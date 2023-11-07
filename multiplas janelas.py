import tkinter as tk

#CRIANDO JANELA PRINCIPAL
janela = tk.Tk()


def abrirJanela(): #CRIANDO COMANDO NOVA JANELA
    janela2 = tk.Toplevel()
    janela2.title('Inserir palavra')
    texto = tk.Label(janela2, text='Insira nova palavra')
    texto.grid(row=0, column=0)
    botao_sair = tk.Button(master=janela2, text='SAIR', command=janela2.destroy)
    botao_sair.grid(row=1, column=0)


#CRIANDO BOTÃO DE NOVA JANELA
botao1 = tk.Button(master=janela, text='adicionar nova palavra', command=abrirJanela)
botao1.grid(row=1, column=0)

#LENDO O ARQUIVO TXT
def lerArquivo():
    arquivo = open('palavras.txt', 'r')
    palavras = [x for x in arquivo.read().split(', ')]
    print(palavras)
    arquivo.close()
    return palavras

texto_palavras = ''
for palavra in lerArquivo():
    texto_palavras+=f'{palavra}, '
texto_palavras = texto_palavras[0:-2] 

label_palavras = tk.Label(janela, text=texto_palavras)
label_palavras.grid(row=0, column=0)

janela.mainloop()