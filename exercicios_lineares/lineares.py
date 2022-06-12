import random

from pdf_base.pdf_base import PDF

print('Gerador de Calculos Matematicos')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = int(input('Digite o primeiro numero do intervalo: '))
intervalo2 = int(input('Digite o ultimo numero do intervalo: '))
ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')
operador = input('Digite o Operador:(Divisão = ÷ / Multiplicação = x / Soma = + / Subtração = - ) ')

titulo = 'GCM - Gerador de Calcúlos Matematicos'
pdf = PDF(titulo=titulo, cabecario=cabecario, imagem='65709.png')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('courier', '', 14)


def gerando_numeros():
    fator1 = random.randint(intervalo1, intervalo2)
    fator2 = random.randint(intervalo1, intervalo2)
    return fator1, fator2


class ExerciciosLineares:
    def __init__(self, operador, gerador, pdf, ordem):
        self.operador = operador
        self.gerador = gerador
        self.pdf = pdf
        self.linha = 27
        self.linha2 = 35
        self.coluna = 10
        self.tamanho_altura = 8
        self.tamanho_largura = 80
        self.x1 = 60
        self.x = 1
        self.fator1 = None
        self.fator2 = None
        self.ordem = ordem

    def exercicios(self):
        if self.ordem == 'n':
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador()
                if self.linha < 260 and self.coluna == 10:
                    self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                        f'{self.x}) {self.fator1} {self.operador} {self.fator2} =', border=True)
                    self.pdf.set_xy(self.coluna, self.linha + 8)
                    self.linha = self.linha + 8

                else:
                    self.coluna = 100
                    self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                        f'{self.x}) {self.fator1} {self.operador} {self.fator2} =', border=True)
                    self.pdf.set_xy(self.coluna, self.linha2 + 8)
                    self.linha2 = self.linha2 + 8
                self.x = self.x + 1
        else:
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador()
                if self.fator1 > self.fator2:
                    if self.linha < 260 and self.coluna == 10:
                        self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                            f'{self.x}) {self.fator1} {self.operador} {self.fator2} =', border=True)
                        self.pdf.set_xy(self.coluna, self.linha + 8)
                        self.linha = self.linha + 8

                    else:
                        self.coluna = 100
                        self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                            f'{self.x}) {self.fator1} {self.operador} {self.fator2} =', border=True)
                        self.pdf.set_xy(self.coluna, self.linha2 + 8)
                        self.linha2 = self.linha2 + 8
                else:
                    if self.linha < 260 and self.coluna == 1:
                        self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                            f'{self.x}) {self.fator2} {self.operador} {self.fator1} =', border=True)
                        self.pdf.set_xy(self.coluna, self.linha + 8)
                        self.linha = self.linha + 8
                    else:
                        self.coluna = 100
                        self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                                            f'{self.x}) {self.fator2} {self.operador} {self.fator1} =', border=True)
                        self.pdf.set_xy(self.coluna, self.linha2 + 8)
                        self.linha2 = self.linha2 + 8
                self.x = self.x + 1

        return self.pdf.output('multiplicacao_novo.pdf')


exercicios = ExerciciosLineares(operador=operador, gerador=gerando_numeros, pdf=pdf, ordem=ordem).exercicios()

