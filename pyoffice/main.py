import argparse
import sys
from pyoffice.pdf.pdfconv import pdf2txt


def main():
    """ Entry point for the pyoffice CLI.
    """
    parser = argparse.ArgumentParser(description='pyoffice - Office-related tasks')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    # Sub-parser for the pdf2read command
    pdf2txt_parser = subparsers.add_parser('pdf2read', description='Extract the text content of a PDF file')
    pdf2txt_parser.add_argument('input', help='Input PDF file path')
    pdf2txt_parser.add_argument('-o', '--output', default=None, required=False, help='Output text file path')

    args = parser.parse_args()

    if args.command == 'pdf2read':
        pdf2txt(args.input, args.output)
    else:
        # Display help and available commands
        parser.print_help()
        print('\nAvailable commands:')
        for choice, subparser in subparsers.choices.items():
            print(f'{choice}: {subparser.description}')

if __name__ == '__main__':
    main()

