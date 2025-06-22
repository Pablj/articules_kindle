from ebooklib import epub
from bs4 import BeautifulSoup

def convert_html_to_epub(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title('Artículo convertido')
    book.set_language('es')

    chapter = epub.EpubHtml(title='Contenido', file_name='chap_01.xhtml', lang='es')
    chapter.content = str(soup)

    book.add_item(chapter)
    book.toc = (epub.Link('chap_01.xhtml', 'Contenido', 'intro'),)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = ['nav', chapter]

    epub_path = html_path.replace('.html', '.epub')
    epub.write_epub(epub_path, book, {})
    return epub_path
