def num():
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByName('Python_macro1')
    A3 = sheet.getCellRangeByName('A3')
    B3 = sheet.getCellRangeByName('B3')
    A4 = sheet.getCellRangeByName('A4')
    A5 = sheet.getCellRangeByName('A5')
    B4 = sheet.getCellRangeByName('B4')
    B5 = sheet.getCellRangeByName('B5')

    A3.Value = 222
    B3.Value = 555

    A4.Value = A3.Value + B3.Value
    A5.Value = B3.Value - A3.Value
    B4.Value = A3.Value * B3.Value
    B5.Value = A3.Value / B3.Value
