def hello():
	doc = XSCRIPTCONTEXT.getDocument()
	sheet = doc.getSheets().getByName('Python_macro1')
	A1 = sheet.getCellRangeByName('A1')
	B1 = sheet.getCellRangeByName('B1')
	A2 = sheet.getCellRangeByName('A2')
	B2 = sheet.getCellRangeByName('B2')
	A1.String = 'Hello'
	B1.String = 'World'
	A2.String = A1.String + B1.String
	B2.String = A1.String + B1.String + '1234'
