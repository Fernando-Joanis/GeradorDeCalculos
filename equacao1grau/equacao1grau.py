import random
from fpdf import FPDF
print('Gerador de Calculos Matematicos (EQUAÇÃO DE 1 GRAU)')
print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
cabecario = input('Insira o Cabeçario desejado: ')
dificuldade = input('Selecione a dificuldade das equações: [0] Muito Facil [1]Facil [2]Médio [3]Dificil [4]Muito Dificil:  ')
x1 = 8

class PDF(FPDF):
    def header(self):
        self.image('65709.png', 1, 1, 2)
        self.set_font('courier', 'BIU', 16)
        self.set_text_color(220, 50, 50)
        self.cell(0, 1.5, 'Gerador de calculos Matemáticos - Equação 1º Grau', border=False, ln=True, align='R')
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

if dificuldade == '0':
    x = 1
    while x <= x1:
        fator1 = random.randint(1, 4)
        fator2 = random.randint(1, 4)
        fator3 = random.randint(1, 4)
        resposta = int((fator1 * fator3) + fator2)

        if resposta == int((fator1 * fator3) + fator2):
            if linha < 26 and coluna == 1:
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha + 3)
                linha = linha + 3

            else:
                coluna = 10
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha2 + 3)
                linha2 = linha2 + 3
            x = x + 1
        else:
            continue

elif dificuldade == '1':
    x = 1
    while x <= x1:
        fator1 = random.randint(1, 9)
        fator2 = random.randint(1, 9)
        fator3 = random.randint(1, 9)
        resposta = int((fator1 * fator3) + fator2)

        if resposta == int((fator1 * fator3) + fator2):
            if linha < 26 and coluna == 1:
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha + 3)
                linha = linha + 3

            else:
                coluna = 10
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha2 + 3)
                linha2 = linha2 + 3
            x = x + 1
        else:
            continue
elif dificuldade == '2':
    x = 1
    while x <= x1:
        fator1 = random.randint(1, 20)
        fator2 = random.randint(1, 20)
        fator3 = random.randint(1, 20)
        resposta = int((fator1 * fator3) + fator2)

        if resposta == int((fator1 * fator3) + fator2):
            if linha < 26 and coluna == 1:
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha + 3)
                linha = linha + 3

            else:
                coluna = 10
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha2 + 3)
                linha2 = linha2 + 3
            x = x + 1
        else:
            continue
elif dificuldade =='3':
    x = 1
    while x <= x1:
        fator1 = random.randint(1, 100)
        fator2 = random.randint(1, 100)
        fator3 = random.randint(1, 100)
        resposta = int((fator1 * fator3) + fator2)

        if resposta == int((fator1 * fator3) + fator2):
            if linha < 26 and coluna == 1:
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha + 3)
                linha = linha + 3

            else:
                coluna = 10
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha2 + 3)
                linha2 = linha2 + 3
            x = x + 1
        else:
            continue
else:
    x = 1
    while x <= x1:
        fator1 = random.randint(10, 999)
        fator2 = random.randint(10, 999)
        fator3 = random.randint(10, 999)
        resposta = int((fator1 * fator3) + fator2)

        if resposta == int((fator1 * fator3) + fator2):
            if linha < 26 and coluna == 1:
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha + 3)
                linha = linha + 3

            else:
                coluna = 10
                pdf.multi_cell(15, 1, (f'{x}) {fator1}x + {fator2}= {resposta}'), border='T')
                pdf.set_xy(coluna, linha2 + 3)
                linha2 = linha2 + 3
            x = x + 1
        else:
            continue

pdf.output('equacao_1_grau_2.pdf')
