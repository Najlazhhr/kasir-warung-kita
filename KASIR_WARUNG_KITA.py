from datetime import datetime

# ======================================
# DATA PRODUK
# ======================================

data_produk = {
    'P001': {'nama': 'Beras 1kg', 'harga': 15000, 'stok': 50},
    'P002': {'nama': 'Minyak Goreng 1L', 'harga': 20000, 'stok': 30},
    'P003': {'nama': 'Gula Pasir 1kg', 'harga': 14000, 'stok': 40},
    'P004': {'nama': 'Mie Instan', 'harga': 3500, 'stok': 100}
}

riwayat_transaksi = []


# ======================================
# TAMPILKAN KATALOG
# ======================================

def tampil_katalog():
    print("\n===== KATALOG BARANG =====")

    for kode, barang in data_produk.items():
        print(
            f"{kode} | {barang['nama']} | "
            f"Harga: Rp{barang['harga']:,} | "
            f"Stok: {barang['stok']}"
        )


# ======================================
# TAMBAH PRODUK
# ======================================

def tambah_produk():

    print("\n===== TAMBAH PRODUK =====")

    kode = input("Masukkan kode produk: ").upper()

    if kode in data_produk:
        print("Kode produk sudah digunakan!")
        return

    nama = input("Masukkan nama produk: ")

    try:
        harga = int(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))

        if harga <= 0 or stok < 0:
            print("Harga dan stok harus bernilai positif.")
            return

    except ValueError:
        print("Harga dan stok harus berupa angka.")
        return

    data_produk[kode] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    print(f"Produk '{nama}' berhasil ditambahkan.")


# ======================================
# TRANSAKSI
# ======================================

def transaksi():

    daftar_belanja = []
    total = 0

    while True:

        tampil_katalog()

        kode = input("\nMasukkan kode barang (ketik SELESAI jika selesai): ").upper()

        if kode == "SELESAI":
            break

        if kode not in data_produk:
            print("Kode barang tidak ditemukan!")
            continue

        produk = data_produk[kode]

        while True:

            try:
                jumlah = int(input(f"Jumlah {produk['nama']} (Stok: {produk['stok']}): "))

                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    continue

                if jumlah > produk["stok"]:
                    print(f"Stok tidak cukup! Sisa stok: {produk['stok']}")
                    continue

                break

            except ValueError:
                print("Input harus berupa angka!")

        subtotal = jumlah * produk["harga"]

        produk["stok"] -= jumlah

        total += subtotal

        daftar_belanja.append({
            "kode": kode,
            "nama": produk["nama"],
            "jumlah": jumlah,
            "harga": produk["harga"],
            "subtotal": subtotal
        })

    if total == 0:
        print("Tidak ada transaksi.")
        return

    # ==========================
    # HITUNG DISKON
    # ==========================

    if total >= 100000:
        diskon = int(total * 0.10)
    else:
        diskon = 0

    bayar = total - diskon

    # ==========================
    # TAMPILKAN TOTAL PEMBAYARAN
    # ==========================

    print("\n===================================")
    print("          PEMBAYARAN")
    print("===================================")
    print(f"Total Belanja : Rp{total:,}")
    print(f"Diskon        : Rp{diskon:,}")
    print(f"Total Bayar   : Rp{bayar:,}")
    print("===================================")

    # ==========================
    # INPUT UANG PELANGGAN
    # ==========================

    while True:

            try:

                uang = int(input("Masukkan uang tunai pelanggan : Rp"))

                # Uang tidak boleh 0 atau negatif
                if uang <= 0:
                    print("Uang harus lebih dari Rp0!")
                    continue

                # Uang kurang
                if uang < bayar:
                    print("\n========== PEMBAYARAN GAGAL ==========")
                    print(f"Total Bayar : Rp{bayar:,}")
                    print(f"Uang Masuk  : Rp{uang:,}")
                    print(f"Kekurangan  : Rp{bayar - uang:,}")
                    print("Silakan masukkan uang yang cukup.")
                    print("=====================================")
                    continue

                # Hitung kembalian
                kembalian = uang - bayar
                break

            except ValueError:
                print("Input harus berupa angka!")

    # ==========================
    # SIMPAN TRANSAKSI
    # ==========================

    id_transaksi = f"TRX{len(riwayat_transaksi)+1:03d}"

    data_transaksi = {
        "id_transaksi": id_transaksi,
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "barang": daftar_belanja,
        "total": total,
        "diskon": diskon,
        "bayar": bayar,
        "uang": uang,
        "kembalian": kembalian
    }

    riwayat_transaksi.append(data_transaksi)

    print("\n===================================")
    print("     TRANSAKSI BERHASIL")
    print("===================================")
    print(f"Total Bayar   : Rp{bayar:,}")
    print(f"Uang Tunai    : Rp{uang:,}")
    print(f"Kembalian     : Rp{kembalian:,}")
    print("===================================")

# ======================================
# CETAK STRUK
# ======================================

def cetak_struk():

    if not riwayat_transaksi:
        print("Belum ada transaksi.")
        return

    trx = riwayat_transaksi[-1]

    print("\n========== STRUK ==========")
    print("ID      :", trx["id_transaksi"])
    print("Waktu   :", trx["waktu"])
    print("---------------------------")

    for item in trx["barang"]:
        print(
            f"{item['nama']} "
            f"x{item['jumlah']} "
            f"= Rp{item['subtotal']:,}"
        )

    print("---------------------------")
    print(f"Total Belanja : Rp{trx['total']:,}")
    print(f"Diskon        : Rp{trx['diskon']:,}")
    print(f"Total Bayar   : Rp{trx['bayar']:,}")
    print(f"Uang Tunai    : Rp{trx['uang']:,}")
    print(f"Kembalian     : Rp{trx['kembalian']:,}")
    print("===========================")


# ======================================
# CEK STOK
# ======================================

def cek_stok():

    print("\n===== STOK BARANG =====")

    for kode, barang in data_produk.items():
        print(
            f"{kode} | "
            f"{barang['nama']} | "
            f"Stok: {barang['stok']}"
        )


# ======================================
# RIWAYAT TRANSAKSI
# ======================================

def tampilkan_riwayat():

    print("\n===== RIWAYAT TRANSAKSI =====")

    if not riwayat_transaksi:
        print("Belum ada transaksi.")
        return

    laporan = sorted(
        riwayat_transaksi,
        key=lambda x: x["bayar"],
        reverse=True
    )

    total_omset = 0

    print(
    f"{'ID TRX':<10} | "
    f"{'WAKTU':<19} | "
    f"{'TOTAL':<12} | "
    f"{'UANG':<12} | "
    f"{'KEMBALIAN':<12}"
)

    print("-" * 50)

    for trx in laporan:

        print(
    f"{trx['id_transaksi']:<10} | "
    f"{trx['waktu']:<19} | "
    f"Rp{trx['bayar']:<10,} | "
    f"Rp{trx['uang']:<10,} | "
    f"Rp{trx['kembalian']:<10,}"
)

        total_omset += trx["bayar"]

    print("-" * 50)
    print(f"Total Omset Penjualan : Rp{total_omset:,}")


# ======================================
# MENU UTAMA
# ======================================

while True:

    print("""
=================================
         SELAMAT DATANG
              DI
  APLIKASI KASIR WARUNG KITA
=================================
1. Tampilkan Katalog
2. Tambah Produk
3. Transaksi
4. Cetak Struk
5. Cek Stok
6. Riwayat Transaksi
7. Keluar
=================================
""")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampil_katalog()

    elif pilihan == "2":
        tambah_produk()

    elif pilihan == "3":
        transaksi()

    elif pilihan == "4":
        cetak_struk()

    elif pilihan == "5":
        cek_stok()

    elif pilihan == "6":
        tampilkan_riwayat()

    elif pilihan == "7":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Menu tidak tersedia.")