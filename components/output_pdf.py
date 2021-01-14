from fpdf import FPDF

q_player1 = []
a_player1 = []
c_player1 = []

q_player2 = []
a_player2 = []
c_player2 = []


def output(player, q_list, a_list, c_list):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('Roboto', '', 'font/Roboto-Regular.ttf', uni=True)
    pdf.set_font('Roboto', '', 20)

    pdf.cell(200, 10, f'Hráč {player}', 0, 1, 'C')

    pdf.set_font('Roboto', '', 10)
    
    for idx, line in enumerate(q_list):
        # Otázka
        pdf.set_text_color(0, 0, 0)
        pdf.cell(40, 10, q_list[idx], 0, 1)

        # Odpověď
        try:
            if c_list[idx] == 1:
                pdf.set_text_color(0, 255, 0)
            else:
                pdf.set_text_color(255, 0, 0)
            pdf.cell(180, 10, a_list[idx], 0, 1, 'R')
        except IndexError:
            raise Exception("Program byl příliš brzo ukončen!")

        if idx == 11:
            pdf.cell(40, 10, '', 0, 1)

    pdf.output(f'hrac{player}.pdf', 'F')
