# ======================================
# APLIKASI KASIR WARUNG KITA
# ======================================

# Dictionary Data Produk
data_produk = {
    'P001': {'nama': 'Beras 1kg', 'harga': 15000, 'stok': 50},
    'P002': {'nama': 'Minyak Goreng 1L', 'harga': 20000, 'stok': 30},
    'P003': {'nama': 'Gula Pasir 1kg', 'harga': 14000, 'stok': 40},
    'P004': {'nama': 'Mie Instan', 'harga': 3500, 'stok': 100}
}

# List Riwayat Transaksi
riwayat_transaksi = []


# ===============================
# 1. Katalog Barang
# ===============================
def tampil_katalog():
    print("\n===== KATALOG BARANG =====")
    for kode, barang in data_produk.items():
        print(f"{kode} | {barang['nama']} | Harga: Rp{barang['harga']} | Stok: {barang['stok']}")


# ===============================
# 2. Tambah Barang
# ===============================
def tambah_barang():
    print("\n===== TAMBAH BARANG =====")

    kode = input("Kode Barang : ").upper()

    if kode in data_produk:
        print("Kode sudah digunakan!")
        return

    nama = input("Nama Barang : ")
    harga = int(input("Harga Barang : "))
    stok = int(input("Stok Barang : "))

    data_produk[kode] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    print("Barang berhasil ditambahkan.")


# ===============================
# 3. Transaksi
# ===============================
def transaksi():

    daftar_belanja = []
    total = 0

    while True:

        tampil_katalog()

        kode = input("\nMasukkan kode barang (ketik SELESAI jika selesai): ").upper()

        if kode == "SELESAI":
            break

        # SEARCHING
        if kode in data_produk:

            jumlah = int(input("Jumlah beli : "))

            if jumlah <= data_produk[kode]["stok"]:

                subtotal = jumlah * data_produk[kode]["harga"]

                total += subtotal

                data_produk[kode]["stok"] -= jumlah

                daftar_belanja.append({
                    "nama": data_produk[kode]["nama"],
                    "jumlah": jumlah,
                    "subtotal": subtotal
                })

            else:
                print("Stok tidak mencukupi!")

        else:
            print("Kode barang tidak ditemukan!")

    if total == 0:
        print("Tidak ada transaksi.")
        return

    # Diskon
    if total >= 100000:
        diskon = total * 0.10
    else:
        diskon = 0

    bayar = total - diskon

    riwayat_transaksi.append({
        "barang": daftar_belanja,
        "total": total,
        "diskon": diskon,
        "bayar": bayar
    })

    print("\nTransaksi berhasil.")


# ===============================
# 4. Cetak Struk
# ===============================
def cetak_struk():

    if len(riwayat_transaksi) == 0:
        print("Belum ada transaksi.")
        return

    data = riwayat_transaksi[-1]

    print("\n========== STRUK ==========")

    for item in data["barang"]:
        print(f"{item['nama']} x{item['jumlah']} = Rp{item['subtotal']}")

    print("---------------------------")
    print("Total   : Rp", data["total"])
    print("Diskon  : Rp", data["diskon"])
    print("Bayar   : Rp", data["bayar"])
    print("===========================")


# ===============================
# 5. Cek Stok
# ===============================
def cek_stok():

    print("\n===== STOK BARANG =====")

    for kode, barang in data_produk.items():
        print(f"{kode} | {barang['nama']} | Stok : {barang['stok']}")


# ===============================
# 6. Riwayat Transaksi
# ===============================
def tampil_riwayat():

    if len(riwayat_transaksi) == 0:
        print("Belum ada transaksi.")
        return

    print("\n===== RIWAYAT TRANSAKSI =====")

    # SORTING
    laporan = sorted(
        riwayat_transaksi,
        key=lambda x: x["bayar"],
        reverse=True
    )

    pendapatan = 0

    for i, data in enumerate(laporan, start=1):

        print(f"\nTransaksi {i}")

        for item in data["barang"]:
            print(f"{item['nama']} x{item['jumlah']}")

        print("Total :", data["bayar"])

        pendapatan += data["bayar"]

    print("\nPendapatan Hari Ini : Rp", pendapatan)


# ===============================
# MENU
# ===============================

while True:

    print("""
========== WARUNG MADURA ==========
1. Tampilkan Katalog
2. Tambah Barang
3. Transaksi
4. Cetak Struk
5. Cek Stok
6. Riwayat Transaksi
7. Keluar
===================================
""")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        tampil_katalog()

    elif pilih == "2":
        tambah_barang()

    elif pilih == "3":
        transaksi()

    elif pilih == "4":
        cetak_struk()

    elif pilih == "5":
        cek_stok()

    elif pilih == "6":
        tampil_riwayat()

    elif pilih == "7":
        print("Terima kasih.")
        break

    else:
        print("Menu tidak tersedia.")
