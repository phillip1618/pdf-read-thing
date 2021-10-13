# pdf-read-thing

## Setup/Usage

1. Clone the repo: `git clone https://github.com/phillip1618/pdf-read-thing.git`
2. Install Python 3
3. Change current working directory to the project directory
4. Run: `python3 -m venv venv`
5. If on Windows, run: `venv\Scripts\activate.bat`. Otherwise if on macOS, run: `source venv/bin/activate`
6. Run `pip install -r requirements.txt`
7. Create a "data" directory in the project directory
8. Place all the pdf's in the data directory
9. Run `python pdf_main.py`
10. A "data.csv" should be generated in the data directory

Some resources:

- <https://github.com/pymupdf/PyMuPDF-Utilities/tree/master/textbox-extraction>
- <https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/textbox-extraction/textbox-extract-1.py>
