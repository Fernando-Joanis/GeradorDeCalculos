from fpdf import FPDF
import random

print('Gerador de Calculos Matematicos (SOMA)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = input('Digite o primeiro numero do intervalo: ')
intervalo2 = input('Digite o ultimo numero do intervalo: ')
ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')

intervalo1 = int(intervalo1)
intervalo2 = int(intervalo2)
x1 = 56


class PDF(FPDF):
    def header(self):
        self.image('65709.png', 1, 1, 2)
        self.set_font('courier', 'BIU', 17)
        self.set_text_color(220, 50, 50)
        self.cell(0, 1.5, 'Gerador de calculos Matemáticos - SOMA', border=False, ln=True, align='R')
        self.set_font('courier', 'IU', 15)
        self.set_text_color(0, 0, 0)
        self.cell(0, 0, cabecario, border=False, ln=True, align='R')
        self.ln(2)

    def footer(self):
        self.set_y(28)
        self.set_font('courier', 'I', 10)
        self.cell(0, 1, f'Página {self.page_no()}/{{nb}}', align='C')


pdf = PDF('P', 'cm', 'A4')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.set_font('courier', '', 14)
linha = 4.5
linha2 = 3.7
coluna = 1

if ordem == 'n':
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if linha < 26 and coluna == 1:
            pdf.multi_cell(8, 0.8, (f'{x}) {fator1} + {fator2} ='), border=True)
            pdf.set_xy(coluna, linha + 0.8)
            linha = linha + 0.8

        else:
            coluna = 10
            pdf.multi_cell(8, 0.8, (f'{x}) {fator1} + {fator2} ='), border=True)
            pdf.set_xy(coluna, linha2 + 0.8)
            linha2 = linha2 + 0.8
        x = x + 1
else:
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if fator1 > fator2:
            if linha < 26 and coluna == 1:
                pdf.multi_cell(8, 0.8, (f'{x}) {fator1} + {fator2} ='), border=True)
                pdf.set_xy(coluna, linha + 0.8)
                linha = linha + 0.8

            else:
                coluna = 10
                pdf.multi_cell(8, 0.8, (f'{x}) {fator1} + {fator2} ='), border=True)
                pdf.set_xy(coluna, linha2 + 0.8)
                linha2 = linha2 + 0.8
        else:
            if linha < 26 and coluna == 1:
                pdf.multi_cell(8, 0.8, (f'{x}) {fator2} + {fator1} ='), border=True)
                pdf.set_xy(coluna, linha + 0.8)
                linha = linha + 0.8
            else:
                coluna = 10
                pdf.multi_cell(8, 0.8, (f'{x}) {fator2} + {fator1} ='), border=True)
                pdf.set_xy(coluna, linha2 + 0.8)
                linha2 = linha2 + 0.8
        x = x + 1
pdf.output('soma_1.pdf')
