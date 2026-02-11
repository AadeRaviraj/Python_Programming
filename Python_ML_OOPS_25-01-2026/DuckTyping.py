# Duck typing : It is a concept where the type of an object it determine by its behavior , not by its class 

class InkjetPrinter:
    def PrintDocument(self,document):
        print("InkJet  printer printing  : ",document)

class LaserPrinter:
    def PrintDocument(self,document):
        print("Laser  printer printing : ",document)
        
        
class PdfWriter:
    def PrintDocument(self,document):
        print(f"Saving  {document} as pdf")
        
def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")


def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PdfWriter())


main()