from fpdf import FPDF
import random

print('Gerador de Calculos Matematicos (SOMA)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
# cabecario = input('Insira o Cabeçario desejado: ')
# intervalo1 = input('Digite o primeiro numero do intervalo: ')
# intervalo2 = input('Digite o ultimo numero do intervalo: ')
# ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')

# intervalo1 = int(intervalo1)
# intervalo2 = int(intervalo2)
x1 = 36
intervalo1 = 1
intervalo2 = 20
ordem = 'n'

class PDF(FPDF):
    def header(self):
        self.image('65709.png', 1, 1, 2)
        self.set_font('courier', 'BIU', 17)
        self.set_text_color(220, 50, 50)
        self.cell(0, 1.5, 'Gerador de calculos Matemáticos - SOMA', border=False, ln=True, align='R')
        self.set_font('courier', 'IU', 15)
        self.set_text_color(0, 0, 0)
        # self.cell(0, 0, cabecario, border=False, ln=True, align='R')
        self.ln(2)

    def footer(self):
        self.set_y(28)
        self.set_font('courier', 'I', 10)
        self.cell(0, 1, f'Página {self.page_no()}/{{nb}}', align='C')


pdf = PDF('P', 'cm', 'A4')
pdf.alias_nb_pages()
pdf.accept_page_break()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('courier', '', 14)
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
        if x <= 9:
            pdf.set_xy(coluna1, linha + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.multi_cell(3, 0.8, f'+ {fator2}', border='B', align='R')
            pdf.set_xy(coluna1, linha + 2.8)
            linha = linha + 2.8

        elif x >= 10 and x <= 18:
            pdf.set_xy(coluna2, linha2 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna2, linha2 + 3.6)
            pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

            linha2 = linha2 + 2.8

        elif x >= 19 and x <= 27:
            pdf.set_xy(coluna3, linha3 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna3, linha3 + 3.6)
            pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

            linha3 = linha3 + 2.8

        else:
            pdf.set_xy(coluna4, linha4 + 2.8)
            pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
            pdf.set_xy(coluna4, linha4 + 3.6)
            pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

            linha4 = linha4 + 2.8
        x = x + 1
else:
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if fator1 > fator2:
            if x <= 9:
                pdf.set_xy(coluna1, linha + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.multi_cell(3, 0.8, f'+ {fator2}', border='B', align='R')
                pdf.set_xy(coluna1, linha + 2.8)
                linha = linha + 2.8

            elif x >= 10 and x <= 18:
                pdf.set_xy(coluna2, linha2 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna2, linha2 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

                linha2 = linha2 + 2.8

            elif x >= 19 and x <= 27:
                pdf.set_xy(coluna3, linha3 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna3, linha3 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

                linha3 = linha3 + 2.8

            else:
                pdf.set_xy(coluna4, linha4 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator1}', align='R')
                pdf.set_xy(coluna4, linha4 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator2}', border='B', align='R')

                linha4 = linha4 + 2.8
        else:
            if x <= 9:
                pdf.set_xy(coluna1, linha + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.multi_cell(3, 0.8, f'+ {fator1}', border='B', align='R')
                pdf.set_xy(coluna1, linha + 2.8)
                linha = linha + 2.8

            elif x >= 10 and x <= 18:
                pdf.set_xy(coluna2, linha2 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna2, linha2 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator1}', border='B', align='R')

                linha2 = linha2 + 2.8

            elif x >= 19 and x <= 27:
                pdf.set_xy(coluna3, linha3 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna3, linha3 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator1}', border='B', align='R')

                linha3 = linha3 + 2.8

            else:
                pdf.set_xy(coluna4, linha4 + 2.8)
                pdf.multi_cell(3, 0.8, f'{x}) {fator2}', align='R')
                pdf.set_xy(coluna4, linha4 + 3.6)
                pdf.multi_cell(3, 0.8, f' + {fator1}', border='B', align='R')

                linha4 = linha4 + 2.8
        x = x + 1
pdf.output('soma_montada_1.pdf')
