# Mengimpor class yang dibutuhkan dari package pengeluaran.
from pengeluaran import PengelolaPengeluaran, FilePengeluaran, AnalisisPengeluaran
from pengeluaran.validasi import validasi_tanggal, validasi_nominal

def tampilkan_menu():
    print("\n=== MANAJEMEN PENGELUARAN HARIAN ===")
    print("1. Buat file data")
    print("2. Tambah pengeluaran")
    print("3. Tampilkan semua data")
    print("4. Lihat analisis dan buat laporan")
    print("5. Keluar")

# Fungsi utama yang menjalankan seluruh proses program.
def main():
    penyimpanan = FilePengeluaran(nama_file="data_pengeluaran.txt")
    pengelola = PengelolaPengeluaran()
    analisis = AnalisisPengeluaran()

    # Mengulang menu sampai pengguna memilih keluar.
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            print(penyimpanan.buat_file())

         # Menambahkan data pengeluaran baru
        elif pilihan == "2":
            try:
                tanggal = validasi_tanggal(input("Tanggal (YYYY-MM-DD): ").strip())
                kategori = input("Kategori (Makan/Transportasi/Kuliah/Lainnya): ").strip()
                keterangan = input("Keterangan: ").strip()
                nominal = validasi_nominal(input("Nominal (Rp): ").strip())

                catatan = pengelola.buat_catatan(
                    tanggal=tanggal, kategori=kategori,
                    keterangan=keterangan, nominal=nominal
                )
                penyimpanan.tambah(catatan)
                print("Pengeluaran berhasil disimpan.")
             # Menangani kesalahan input dari pengguna.
            except ValueError as error:
                print(f"Input tidak valid: {error}")
              # Menangani kondisi ketika file data belum tersedia.
            except FileNotFoundError:
                print("File data belum dibuat. Pilih menu 1 terlebih dahulu.")

        elif pilihan == "3":
            daftar = penyimpanan.baca_semua()
            if daftar:
                print("\nDAFTAR PENGELUARAN")
                 # Menampilkan data satu per satu dengan nomor urut.
                for nomor, catatan in enumerate(daftar, start=1):
                    print(
                        f"{nomor}. {catatan.tanggal} | {catatan.kategori} | "
                        f"{catatan.keterangan} | Rp{catatan.nominal:,.0f}".replace(",", ".")
                    )
            else:
                print("Belum ada data pengeluaran yang valid.")

        elif pilihan == "4":
            daftar = penyimpanan.baca_semua()
            laporan = analisis.buat_laporan(daftar)
            print("\n" + laporan)
            try:
                penyimpanan.tulis_laporan(laporan)
                print("Laporan disimpan ke laporan_pengeluaran.txt")
            except OSError as error:
                print(f"Laporan gagal disimpan: {error}")

        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak tersedia. Masukkan angka 1 sampai 5.")

if __name__ == "__main__":
    main()
