from escpos.printer import Usb
import time
        
def ImpresionTest():
    p = Usb(0x067b, 0x2305, 0, profile="TM-T88II")
    p.text(time.strftime("%d/%m/%y") + "  -  " + time.strftime("%H:%M:%S"))
    p.text("Hello World\n")
    p.image("/home/pi/Desktop/JPHLogo.gif")
    p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    p.qr("https://www.jphlions.com/",size=8)
    p.cut()
