import random
from fpdf import FPDF

print('Gerador de Calculos Matematicos (MULTIPLICAÇÃO)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = input('Digite o primeiro numero do intervalo: ')
intervalo2 = input('Digite o ultimo numero do intervalo: ')
ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')

intervalo1 = int(intervalo1)
intervalo2 = int(intervalo2)
x1 = 24

class PDF(FPDF):
    def header(self):
        self.image('65709.png', 0.7, 0.7, 1.5)
        self.set_font('arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 1, 'Gerador de calculos Matemáticos - Multiplicação', border=False, ln=True, align='R')
        self.set_font('arial', 'IU', 15)
        self.set_text_color(0, 0, 0)
        self.ln(0.5)
        self.cell(0, 0, cabecario, border=False, ln=True, align='C')
        self.ln(2)

    def footer(self):
        self.set_y(28)
        self.set_font('courier', 'I', 10)
        self.cell(0, 1, f'Página {self.page_no()}/{{nb}}', align='C')


pdf = PDF('P', 'cm', 'A4')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('arial', 'B', 14)
linha = 0.5
linha2 = 0.4
linha3 = 0.4
linha4 = 0.4
coluna1 = 1
coluna2 = 6.5
coluna3 = 12
coluna4 = 17

if ordem == 'n':
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if x <= 6:
            pdf.set_xy(coluna1, linha + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')
            pdf.set_xy(coluna1, linha + 2.8)
            linha = linha + 4.2

        elif x >= 7 and x <= 12:
            pdf.set_xy(coluna2, linha2 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna2, linha2 + 3.6)
            pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

            linha2 = linha2 + 4.2

        elif x >= 13 and x <= 18:
            pdf.set_xy(coluna3, linha3 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna3, linha3 + 3.6)
            pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

            linha3 = linha3 + 4.2

        else:
            pdf.set_xy(coluna4, linha4 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna4, linha4 + 3.6)
            pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

            linha4 = linha4 + 4.2
        x = x + 1
else:
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if fator1 > fator2:
            if x <= 6:
                pdf.set_xy(coluna1, linha + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')
                pdf.set_xy(coluna1, linha + 2.8)
                linha = linha + 4.2

            elif x >= 7 and x <= 12:
                pdf.set_xy(coluna2, linha2 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna2, linha2 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

                linha2 = linha2 + 4.2

            elif x >= 13 and x <= 18:
                pdf.set_xy(coluna3, linha3 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna3, linha3 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

                linha3 = linha3 + 4.2

            else:
                pdf.set_xy(coluna4, linha4 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna4, linha4 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator2}', border='B', align='R')

                linha4 = linha4 + 4.2
        else:
            if x <= 6:
                pdf.set_xy(coluna1, linha + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.multi_cell(3, 0.8, f'X {fator1}', border='B', align='R')
                pdf.set_xy(coluna1, linha + 2.8)
                linha = linha + 4.2

            elif x >= 7 and x <= 12:
                pdf.set_xy(coluna2, linha2 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna2, linha2 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator1}', border='B', align='R')

                linha2 = linha2 + 4.2

            elif x >= 13 and x <= 18:
                pdf.set_xy(coluna3, linha3 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna3, linha3 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator1}', border='B', align='R')

                linha3 = linha3 + 4.2

            else:
                pdf.set_xy(coluna4, linha4 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna4, linha4 + 3.6)
                pdf.multi_cell(3, 0.8, f'X {fator1}', border='B', align='R')

                linha4 = linha4 + 4.2
        x = x + 1

pdf.output('multiplicacao_montada_1.pdf')
