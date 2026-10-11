from pathlib import Path
from .models import Pengeluaran


class FilePengeluaran:
    """Mengelola penyimpanan data pengeluaran dalam file teks."""

    def __init__(self, nama_file="data_pengeluaran.txt"):
        self.nama_file = Path(nama_file)

    def buat_file(self):
        if self.nama_file.exists():
            return f"File {self.nama_file} sudah tersedia."

        self.nama_file.touch()
        return f"File {self.nama_file} berhasil dibuat."

    def tambah(self, catatan):
        if not self.nama_file.exists():
            raise FileNotFoundError(
                "File data belum dibuat. Pilih menu 1 terlebih dahulu."
            )

        with self.nama_file.open("a", encoding="utf-8") as file:
            file.write(catatan.ke_baris() + "\n")

    def baca_semua(self):
        if not self.nama_file.exists():
            return []

        daftar = []

        with self.nama_file.open("r", encoding="utf-8") as file:
            for baris in file:
                if not baris.strip():
                    continue

                try:
                    catatan = Pengeluaran.dari_baris(baris)
                    daftar.append(catatan)
                except (ValueError, TypeError):
                    continue

        return daftar

    def tulis_laporan(self, laporan):
        with open(
            "laporan_pengeluaran.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(laporan)
