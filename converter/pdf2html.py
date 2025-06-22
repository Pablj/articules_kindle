import subprocess

def convert_pdf_to_html(pdf_path):
    html_path = pdf_path.replace('.pdf', '.html')
    subprocess.run(["pdf2htmlEX", pdf_path, html_path], check=True)
    return html_path
