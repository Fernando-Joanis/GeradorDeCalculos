import random
from fpdf import FPDF

print('Gerador de Calculos Matematicos (DIVISÃO)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
intervalo1 = input('Digite o primeiro numero do intervalo: ')
intervalo2 = input('Digite o ultimo numero do intervalo: ')
ordem = input('Deseja organizar com o maior fator primeiro e resto 0? [s]im ou [n]ão: ')

intervalo1 = int(intervalo1)
intervalo2 = int(intervalo2)
x1 = 12

class PDF(FPDF):
    def header(self):
        self.image('65709.png', 0.7, 0.7, 1.5)
        self.set_font('arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 0.5, 'Gerador de calculos Matemáticos - Divisão', border=False, ln=True, align='R')
        self.set_font('arial', 'IU', 15)
        self.set_text_color(0, 0, 0)
        self.ln(1)
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
pdf.set_font('courier', 'B', 18)
linha = 1
linha2 = 0.9
coluna0 = 1
coluna1 = 1.5
coluna3 = 5
coluna5 = 11
coluna2 = 11.5
coluna4 = 15

if ordem == 'n':
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if x <= 6:
            pdf.set_xy(coluna0, linha + 2.8)
            pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
            pdf.set_xy(coluna1, linha + 2.8)
            pdf.multi_cell(3, 0.8, f' {fator1}', align='R')
            pdf.set_font('courier', 'BU', 18)
            pdf.set_xy(coluna3, linha + 2.8)
            pdf.multi_cell(3, 0.8, f'|{fator2} ', align='L')
            pdf.set_font('courier', 'B', 18)

            linha = linha + 4.2

        else:
            pdf.set_xy(coluna5, linha2 + 2.8)
            pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
            pdf.set_xy(coluna2, linha2 + 2.8)
            pdf.multi_cell(3, 0.8, f' {fator1}', align='R')
            pdf.set_font('courier', 'BU', 18)
            pdf.set_xy(coluna4, linha2 + 2.8)
            pdf.multi_cell(3, 0.8, f'|{fator2} ', align='L')
            pdf.set_font('courier', 'B', 18)

            linha2 = linha2 + 4.2

        x = x + 1
else:
    x = 1
    while x <= x1:
        fator1 = random.randint(intervalo1, intervalo2)
        fator2 = random.randint(intervalo1, intervalo2)
        if fator1 > fator2:
            if fator1 % fator2 == 0:
                if fator1 > fator2:
                    if x <= 6:
                        pdf.set_xy(coluna0, linha + 2.8)
                        pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
                        pdf.set_xy(coluna1, linha + 2.8)
                        pdf.multi_cell(3, 0.8, f' {fator1}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(coluna3, linha + 2.8)
                        pdf.multi_cell(3, 0.8, f'|{fator2} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        linha = linha + 4.2

                    else:
                        pdf.set_xy(coluna5, linha2 + 2.8)
                        pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
                        pdf.set_xy(coluna2, linha2 + 2.8)
                        pdf.multi_cell(3, 0.8, f' {fator1}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(coluna4, linha2 + 2.8)
                        pdf.multi_cell(3, 0.8, f'|{fator2} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        linha2 = linha2 + 4.2


                else:
                    if x <= 6:
                        pdf.set_xy(coluna0, linha + 2.8)
                        pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
                        pdf.set_xy(coluna1, linha + 2.8)
                        pdf.multi_cell(3, 0.8, f' {fator2}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(coluna3, linha + 2.8)
                        pdf.multi_cell(3, 0.8, f'|{fator1} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        linha = linha + 4.2

                    else:
                        pdf.set_xy(coluna5, linha2 + 2.8)
                        pdf.multi_cell(1.5, 0.8, f'{x})', align='R')
                        pdf.set_xy(coluna2, linha2 + 2.8)
                        pdf.multi_cell(3, 0.8, f' {fator2}', align='R')
                        pdf.set_font('courier', 'BU', 18)
                        pdf.set_xy(coluna4, linha2 + 2.8)
                        pdf.multi_cell(3, 0.8, f'|{fator1} ', align='L')
                        pdf.set_font('courier', 'B', 18)

                        linha2 = linha2 + 4.2



                x = x + 1

pdf.output('divisao_montada_2.pdf')
