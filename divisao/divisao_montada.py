from pdf_base.pdf_base import PDF
from gerador_numeros.gerador_numeros import gerando_numeros

print('Gerador de Calculos Matematicos (DIVISÃO)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = input('Digite o primeiro numero do intervalo: ')
intervalo2 = input('Digite o ultimo numero do intervalo: ')
ordem = input('Deseja organizar com o maior fator primeiro e resto 0? [s]im ou [n]ão: ')

intervalo1 = int(intervalo1)
intervalo2 = int(intervalo2)

titulo = 'Gerador de calculos Matemáticos - Divisão'

pdf = PDF(titulo=titulo, cabecario=cabecario, imagem='65709.png')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('courier', 'B', 18)


class DivisaoMontada:
    def __init__(self, gerador, ordem, pdf, intervalo1, intervalo2):
        self.gerador = gerador
        self.ordem = ordem
        self.pdf = pdf
        self.linha = 10
        self.linha2 = 9
        self.coluna0 = 10
        self.coluna1 = 15
        self.coluna3 = 50
        self.coluna5 = 110
        self.coluna2 = 115
        self.coluna4 = 150
        self.x1 = 12
        self.x = 1
        self.fator1 = None
        self.fator2 = None
        self.intervalo1 = intervalo1
        self.intervalo2 = intervalo2

    def exercicios(self):
        if self.ordem == 'n':
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador(intervalo1=self.intervalo1, intervalo2=self.intervalo2)
                if self.x <= 6:
                    pdf.set_xy(self.coluna0, self.linha + 28)
                    pdf.multi_cell(15, 8, f'{self.x})', align='R')
                    pdf.set_xy(self.coluna1, self.linha + 28)
                    pdf.multi_cell(30, 8, f' {self.fator1}', align='R')
                    pdf.set_font('courier', 'BU', 18)
                    pdf.set_xy(self.coluna3, self.linha + 28)
                    pdf.multi_cell(30, 8, f'|{self.fator2} ', align='L')
                    pdf.set_font('courier', 'B', 18)

                    self.linha = self.linha + 42

                else:
                    pdf.set_xy(self.coluna5, self.linha2 + 28)
                    pdf.multi_cell(15, 8, f'{self.x})', align='R')
                    pdf.set_xy(self.coluna2, self.linha2 + 28)
                    pdf.multi_cell(30, 8, f' {self.fator1}', align='R')
                    pdf.set_font('courier', 'BU', 18)
                    pdf.set_xy(self.coluna4, self.linha2 + 28)
                    pdf.multi_cell(30, 8, f'|{self.fator2} ', align='L')
                    pdf.set_font('courier', 'B', 18)

                    self.linha2 = self.linha2 + 42

                self.x = self.x + 1
        else:
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador(intervalo1=self.intervalo1, intervalo2=self.intervalo2)
                if self.fator1 % self.fator2 == 0:
                    if self.x <= 6:
                        pdf.set_xy(self.coluna0, self.linha + 28)
                        pdf.multi_cell(15, 8, f'{self.x})', align='R')
                        pdf.set_xy(self.coluna1, self.linha + 28)
                        pdf.multi_cell(30, 8, f' {self.fator1}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(self.coluna3, self.linha + 28)
                        pdf.multi_cell(30, 8, f'|{self.fator2} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        self.linha = self.linha + 42

                    else:
                        pdf.set_xy(self.coluna5, self.linha2 + 28)
                        pdf.multi_cell(15, 8, f'{self.x})', align='R')
                        pdf.set_xy(self.coluna2, self.linha2 + 28)
                        pdf.multi_cell(30, 8, f' {self.fator1}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(self.coluna4, self.linha2 + 28)
                        pdf.multi_cell(30, 8, f'|{self.fator2} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        self.linha2 = self.linha2 + 42

                    self.x = self.x + 1

        return pdf.output('divisao_montada_4.pdf')


exercicios = DivisaoMontada(gerador=gerando_numeros,
                            ordem=ordem,
                            pdf=pdf,
                            intervalo1=intervalo1,
                            intervalo2=intervalo2
                            ).exercicios()

