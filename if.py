aSinifi=["Hilmi","Burak"]
bSinifi=["Ali","Ayşe"]

isim=input("İsim giriniz : ")

if isim in aSinifi:
    print("Kişi a sınıfındadır.")
elif isim in bSinifi:
    print("Kişi b sınıfındadır.")
else:
    print("Kişi sınıflarda bulunamamaktadır ! ")