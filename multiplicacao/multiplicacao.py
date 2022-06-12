import random

from pdf_base.pdf_base import PDF

print('Gerador de Calculos Matematicos (MULTIPLICAÇÃO)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = int(input('Digite o primeiro numero do intervalo: '))
intervalo2 = int(input('Digite o ultimo numero do intervalo: '))
ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')

x1 = 56

titulo = 'Exercicios Matematicos - Multiplicação'
pdf = PDF(titulo=titulo, cabecario=cabecario)
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('courier', '', 14)
linha = 45
linha2 = 37
coluna = 10
tamanho_altura = 8
tamanho_largura = 80


def gerando_numeros():

    fator1 = random.randint(intervalo1, intervalo2)
    fator2 = random.randint(intervalo1, intervalo2)
    return fator1, fator2

if ordem == 'n':
    x = 1
    while x <= x1:
        fator1, fator2 = gerando_numeros()
        if linha < 260 and coluna == 10:
            pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator1} x {fator2} ='), border=True)
            pdf.set_xy(coluna, linha + 8)
            linha = linha + 8

        else:
            coluna = 100
            pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator1} x {fator2} ='), border=True)
            pdf.set_xy(coluna, linha2 + 8)
            linha2 = linha2 + 8
        x = x + 1
else:
    x = 1
    while x <= x1:
        fator1, fator2 = gerando_numeros()
        if fator1 > fator2:
            if linha < 260 and coluna == 10:
                pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator1} x {fator2} ='), border=True)
                pdf.set_xy(coluna, linha + 8)
                linha = linha + 8

            else:
                coluna = 100
                pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator1} x {fator2} ='), border=True)
                pdf.set_xy(coluna, linha2 + 8)
                linha2 = linha2 + 8
        else:
            if linha < 260 and coluna == 1:
                pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator2} x {fator1} ='), border=True)
                pdf.set_xy(coluna, linha + 8)
                linha = linha + 8
            else:
                coluna = 100
                pdf.multi_cell(tamanho_largura, tamanho_altura, (f'{x}) {fator2} x {fator1} ='), border=True)
                pdf.set_xy(coluna, linha2 + 8)
                linha2 = linha2 + 8
        x = x + 1

pdf.output('multiplicacao_1.pdf')
