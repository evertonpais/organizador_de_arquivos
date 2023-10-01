import os
from tkinter import *
from tkinter.filedialog import askdirectory

janela = Tk()
janela.title('organize seus arquivos')
janela.geometry('400x400')

texto_orientacao = Label(janela, text = 'clique no botão para selecionar a pasta que deseja organizar')
texto_orientacao.grid(column=0,row=0)
botao_selecionar = Button(janela, text= 'selecione a pasta',command=askdirectory)  
botao_selecionar.grid(column=0,row=1)
      


janela.mainloop()


caminho = askdirectory(title= 'selecione uma pasta')

lista_arquivos = os.listdir(caminho)


locais = {
    'imagens': ['.png','.jpg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf','.PDF'],
    'documentos do word' : ['.docx'],
    'arquivos jw' : ['.jwpub']
}
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')

   