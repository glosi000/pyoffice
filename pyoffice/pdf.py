import sys
import PyPDF2
from pyoffice.utils import get_files_from_wildcard


def pdf2txt(pdf_path, output_path=None):
    """
    Extracts text content from a PDF file and writes it to a text file or prints it to stdout.

    Parameters
    ----------
    pdf_path : str
        The path to the input PDF file.
    
    output_path : str or None, optional
        The path to the output text file. If not provided, output is redirected to stdout.
        The Default is None.

    Raises
    ------
    FileNotFoundError
        If the specified PDF file does not exist.
    """

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
    else:
        sys.stdout.write(text)

def pdfconcat(output, *args):
    
    pdf_writer = PyPDF2.PdfWriter()

    # Parse all the pdf files
    for i, pdf in enumerate(args):
        try:
            pdf = get_files_from_wildcard(pdf)
            with open(pdf, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)

                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
            sys.stdout.write(f'File {i+1:>4}. - Parsed Successfully!\n')

        except Exception as err:
            sys.stderr.write(f'File {i+1:>4} - ERROR {err}\n')

    # Concat the files and save them
    try:
        with open(output, 'wb') as file:
            pdf_writer.write(file)
        sys.stdout.write(f'Output file generated!\n')
    except:
        sys.stderr.write(f'Output file was NOT generated!\n')

