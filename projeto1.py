from tkinter import *
from tkinter.filedialog import askdirectory
import os
import shutil

def organizar_arquivos():
    caminho = askdirectory(title='Selecione uma pasta')
    if not caminho:
        return

    locais = {
        'imagens': ['.png', '.jpeg','JPEG'],
        'planilhas': ['.xlsx'],
        'pdfs': ['.pdf'],
        'documentos do word': ['.docx'],
        'arquivos jw': ['.jwpub'],
        'videos': ['.mp4']
    }

    lista_arquivos = os.listdir(caminho)
    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        for pasta, extensoes in locais.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(caminho, pasta)
                os.makedirs(pasta_destino, exist_ok=True)
                origem_arquivo = os.path.join(caminho, arquivo)
                destino_arquivo = os.path.join(pasta_destino, arquivo)
                if not os.path.exists(destino_arquivo):
                    shutil.move(origem_arquivo, destino_arquivo)

janela = Tk()
janela.title('Organize seus arquivos')
janela.geometry('400x400')

texto_orientacao = Label(janela, text='Clique no botão para selecionar a pasta que deseja organizar')
texto_orientacao.grid(column=0, row=0)

botao_selecionar = Button(janela, text='Selecione a pasta', command=organizar_arquivos)
botao_selecionar.grid(column=0, row=1)

janela.mainloop()
