'''
Created on Mar 28, 2024

@author: Administrator
'''
from win32 import win32print
from PIL import Image, ImageWin
from pythonwin import win32ui
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
print (printers)

printer_name = win32print.GetDefaultPrinter ()
file_name = "D:/2.pdf"

printer = win32ui.CreateDC ()
printer.CreatePrinterDC (printer_name)

with open(file_name,'rb') as reader:
    pdf_data = reader.read()
printer.StartDoc(file_name)
printer.StartPage ()
printer.PlayMetaFile(pdf_data)
printer.EndPage ()
printer.EndDoc ()
# printer.DeleteDC ()