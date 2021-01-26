nama = input("Tulisakan Nama : ")
umur = input("Umur : ")
status = input("siswa/lulus : ")
if (status == "siswa"):
    sekolah = input ("Asal Sekolah : ")
else:
    lulus = input ("Pekerjaan : ")

print ("Nama : ",nama)
print ("Umur : ",umur)
if (status == "siswa"):
    print ("Asal Sekolah : ", sekolah)
else:
    print ("Pekerjaan : ", lulus)



