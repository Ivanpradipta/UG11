def Pengeluaran(x):
    total=0
    for i in x:
        
        total+=(int(input("Masukkan pengeluaran di bulan"+" "+i+"Rp. ")))
    print("Total pengeluaran selama setahun adalah ", total)

bulan={"januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember",}
Pengeluaran(bulan)
