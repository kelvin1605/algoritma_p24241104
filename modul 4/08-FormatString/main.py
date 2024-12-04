# format string 

"""
    String : kumpulan dari karakter 
    cara membuat String :
    1. dengan single qoute '...'
    2. dengan double qoute "..."
"""
# membuat string dengan single qoute 
nama = 'nama saya kelvin'
print ('kelvin')

#membuat string dengan double qoute 
nama = "nama saya kelvin"
print ("kelvin")

print ("yazid simanjuntak roa rusak")
print ("yazid simanjuntak roa rusak")

# single qoute 
# pakai tanda \

print ('g\'day')
print ('what\'sup')

print('C:\\user\\kelvin')

nama = "kelvin"
print("selamat datang",nama)

# format string 'f' dan '{}'
format_str = f'selamat datang {nama}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 200000
format_str = f'jutaan {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f'desimlal = {angka:.3f}'

# persen 
angka = 0.55 # 0.55 * 100 = 55%
format_str = f'persen = {angka:.1%}'
print(format_str)

# operasi aritmatika dengan format string 
harga = 57250
jumlah = 3

print(f'total bayar : {harga*jumlah:,}')