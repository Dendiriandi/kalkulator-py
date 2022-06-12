print("Kalkulator")
print("1. operasi Penjumlahan")
print("2. operasi Pengurangan")
print("3. operasi Perkalian")
print("4. operasi Pembagian")

pilihan = int(input("\nMasukan Pilihan  : "))

a= int(input("angka 1 : "))
b= int(input("angka 2 : "))

if pilihan == 1:
   hasil = a+b
elif pilihan == 2:
   hasil = a-b
elif pilihan == 3:
   hasil = a*b
elif pilihan == 4:
   hasil = a/b

print("\nHasil : %d" %hasil)