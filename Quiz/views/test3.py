import subprocess
from win32 import win32print
def command_print(event = None):
    try:
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        print (printers)
        command = "{} {}".format('PDFtoPrinter.xe','D:/2.pdf')
        print(command)
        subprocess.call(command,shell=True)
    except Exception as ex:
        print(ex)

command_print()