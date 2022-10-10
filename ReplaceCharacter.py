metin = input("Bir metin giriniz:")
tcharacters=["ç","ı","ü","ö","ğ","ş","Ç","İ","Ü","Ö","Ğ","Ş"]
icharacters=["c","i","u","o","g","s","C","I","U","O","G","S"]
for i in range(12):
  metin= metin.replace(tcharacters[i],icharacters[i])
print(metin)