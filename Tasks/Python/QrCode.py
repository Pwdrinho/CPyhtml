#Gerador de QrCode
#pip install qrcode Pillow
import qrcode

print("---Gerador de QrCode---")
data = input("Digite url que deseja gerar o qrcode: ")
print("---Processando---")

img = qrcode.make(data)

nome_arquivo = data.replace("https://", "").replace("http://", "").replace("/", "_")

img.save(rf"C:\Users\Pedro\Desktop\Programação\QrCode\{nome_arquivo}.png")

print(f"QRCode salvo como {nome_arquivo}.png")
