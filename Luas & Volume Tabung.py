print("Program Python Hitung Luas & Volume Tabung")

pi      = 22/7
jari    = float(input('Masukkan Jari-jari: '))
tinggi  = float(input('Masukkan Tinggi: '))
volume  = pi*jari*jari*tinggi
luas    = 2*pi*jari*(jari+tinggi)

print('hasil')
print('Volume Tabung= ', '{:.2f}'.format(volume))
print('Luas Permukaan Tabung= ', '{:.2f}'.format(luas))
