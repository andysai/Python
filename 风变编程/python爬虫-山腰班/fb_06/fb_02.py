import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'test'
sheet['A1'] = '漫威宇宙'