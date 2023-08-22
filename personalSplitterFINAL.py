from PyPDF2 import PdfReader, PdfWriter
import os

source = r"D:\Asurity\Asurity_Raw_Samples\Asurity_Sample_Docs\_TempFolder\Chris"

def split_PDF (path, start_page: int = 0, stop_page: int = 0):
    with open (path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page - 1, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.splitext(path)[0]
            output_filename = f"{filename}_from_{start_page}_to_{page_num + 1}.pdf"
        with open (output_filename, "wb") as out:
            writer.write(out)

print ("What file would you like to split?")
path = input()
pdf_path = source + '\\' + path + ".pdf"

start_page = 1

try:
    while start_page != 0:
        print("Start page: (Type 0 to stop)")
        start_page = int(input())

        if start_page != 0:
            print("End Page: ")
            stop_page = int(input())
            split_PDF(pdf_path, start_page, stop_page)
        else:
            print("Program stopped.")
            exit()
            
except ValueError:
    print("Value Error. Program stopped.")
except UnboundLocalError:
    print("UnboundLocalError. Program stopped.")
