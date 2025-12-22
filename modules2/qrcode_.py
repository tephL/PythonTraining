import qrcode

while True:
    url = input("URL: ")
    file_path = input("Filename: ")
    
    qr = qrcode.QRCode()
    qr.add_data(url)
    
    img = qr.make_image()
    img.save(file_path + ".png")
    
    print("\n***successfully made qr***\n")
    chc = int(input("[1] Again\n[0] Exit\n> "))
    if chc == 0:
        break 