veri="Eğitim 101"
egitim=list(veri)
print(egitim)
harfSayici=0
rakamSayici=0
for i in egitim:
    if str(i).isdecimal():
        rakamSayici+=1
    else:
        harfSayici+=1

print("Rakam sayısı : ",rakamSayici)
print("Harf sayıcı : ", harfSayici)