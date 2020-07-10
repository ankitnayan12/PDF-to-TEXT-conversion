from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
from os.path import exists

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    print('successfully converted')
    return text 
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" 
    for pdf in os.listdir(pdfDir):
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) 
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w", encoding="utf-8" ) 
            textFile.write(text) 
pdfDir = r'C:/Users/ankit/Dropbox/ankit nitj/code box/submission of text mining1/TASK 1= PDF to TEXT conversion/pdftotxt/pdf/'
txtDir = r'C:/Users/ankit/Dropbox/ankit nitj/code box/submission of text mining1/TASK 1= PDF to TEXT conversion/pdftotxt/txt/'
convertMultiple(pdfDir, txtDir)
#C:/Users/ankit/Dropbox/ankit nitj/code box/submission of text mining1/TASK 1= PDF to TEXT conversion/pdftotxt/pdf/
