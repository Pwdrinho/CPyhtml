import qrcode

def gerar_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

text = "https://www.google.com"
file_name = "qr_code.png"
gerar_qr_code(text, file_name)
print(f"QR Code gerado com sucesso em {file_name}")