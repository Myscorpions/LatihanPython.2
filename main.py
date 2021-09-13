import datetime as dt
print(
    "\n\033[1;93mSilakan Masukan Tanggal, \nbulan dan tahun lahir anda \n"
)
tanggal = int(input("\033[1;37mTanggal \t: "))
bulan = int(input("\033[1;37mBulan \t\t: "))
tahun = int(input("\033[1;37mTahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"\033[1;39mTanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"\033[1;39mHari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"\033[1;39mHari nya adalah : {tanggal_lahir:%A}")
print(
    f"\033[1;39mUmur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan"
)