from fpdf import FPDF

print('Gerador de Calculos Matematicos (Tabuada)')
print('Você precisa escolher o número que deseja utilizar para montar a tabuada!')
numero_tabuada = int(input('Envie o número da tabuada que deseja: '))
cabecario = input('Insira o Cabeçario desejado: ')

class PDF(FPDF):
    def header(self):
        self.image('65709.png', 0.7, 0.7, 1.5)
        self.set_font('arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 0.5, f'Gerador de cálculos Matemáticos - Tabuada do {numero_tabuada}', border=False, ln=True, align='R')
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
var = range(0, 11)
linha = 4
linha2 = 16


for n in var:
    pdf.set_xy(1, linha)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(6, linha)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(11, linha)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(16, linha)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')

    linha = linha + 1

    pdf.set_xy(1, linha2)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(6, linha2)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(11, linha2)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')
    pdf.set_xy(16, linha2)
    pdf.multi_cell(4, 0.8, f'{numero_tabuada} X {n} = ', align='L')

    linha2 = linha2 + 1

pdf.output(f'tabuada_do_{numero_tabuada}.pdf')
