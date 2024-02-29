import random

parola = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifre uzunluğu girin:"))

sifre = ""

for i in range(uzunluk):
    sifre += random.choice(parola)

print(sifre)