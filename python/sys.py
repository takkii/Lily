import sys


def tem():
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByName('Python_macro1')
    A6 = sheet.getCellRangeByName('A6')

    A6.String = (sys.version)
