import sys
import PyPDF2


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

