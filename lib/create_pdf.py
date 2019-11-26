from fpdf import FPDF

def create_pdf(report):
    content = "{}".format(report.content)
    created_at = "{}".format(report.created_at)

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w=180, h=10, txt='Report', ln=2, align='C')
    pdf.cell(w=180, h=10, txt=content, ln=2, align='C')
    pdf.cell(w=180, h=10, txt=created, ln=2, align='C')

    return pdf.output(dest='S').encode('latin-1')
