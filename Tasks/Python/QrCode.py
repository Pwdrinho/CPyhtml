#Gerador de QrCode

import qrcode
import time

def print_progress_bar(progress, end):
    print("[{0}{1}] {2}%".format("█" * progress, "-" * (end - progress), progress), end="\r")
    if progress == end:
        print()

print("--------Gerador de QrCode--------")
data = input("Digite url que deseja gerar o qrcode: ")
print("\n--------Iniciando Processamento-------- \n")


img = qrcode.make(data)

nome_arquivo = input("Digite nome desejado para o QrCode: ")

print("")
for i in range(0, 101):
    print_progress_bar(i, 100)
    time.sleep(0.05)

img.save(rf"C:\Users\Pedro\Desktop\Programação\QrCode\{nome_arquivo}.png")

print(f"\nQRCode salvo como {nome_arquivo}.png \n")
