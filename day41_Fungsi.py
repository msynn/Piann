def suhu_udara (daerah, derajat, satuan = 'Celcius'):
# Parameter :
    # daerah
    # derajat
    # suhu = 'celcius'
    print(f"Suhu di {daerah} adalah {derajat} {satuan}")


# parameter daerah dan derajat wajib di isi,
# tetapi parameter suhu tidak.
suhu_udara("Topoyo", 32)
print('=================================')
# parameter suhu bisa diganti
suhu_udara("Topoyo", 12, 'Reamur')