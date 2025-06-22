from converter.pdf2html import convert_pdf_to_html
from converter.html2epub import convert_html_to_epub
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    html_path = convert_pdf_to_html(pdf_path)
    epub_path = convert_html_to_epub(html_path)

    print(f"EPUB generado: {epub_path}")

if __name__ == "__main__":
    main()
