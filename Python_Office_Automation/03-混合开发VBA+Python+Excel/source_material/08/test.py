# -*- coding: utf-8 -*-
 
import xlwings as xw
 
def say_hi():
    wb = xw.Book.caller()
    sht = wb.sheets[1]
    sht.range('A1').value = '混合开发'
