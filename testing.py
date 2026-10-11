import os
import tempfile
import unittest
from .models import Pengeluaran, PengelolaPengeluaran
from .processing import AnalisisPengeluaran
from .fileio import FilePengeluaran
from .validasi import validasi_tanggal, validasi_nominal

class TestManajemenPengeluaran(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.folder.name, "data.txt")
        self.file_data = FilePengeluaran(self.path)
        self.analisis = AnalisisPengeluaran()

    def tearDown(self):
        self.folder.cleanup()

    def test_membuat_objek_valid(self):
        catatan = Pengeluaran("2026-10-11", "Makan", "Nasi goreng", 15000)
        self.assertEqual(catatan.nominal, 15000)

    def test_nominal_nol_ditolak(self):
        with self.assertRaises(ValueError):
            Pengeluaran("2026-10-11", "Makan", "Nasi", 0)

    def test_kwargs_membuat_catatan(self):
        catatan = PengelolaPengeluaran().buat_catatan(
            tanggal="2026-10-11", kategori="Transportasi",
            keterangan="Bus", nominal=5000
        )
        self.assertEqual(catatan.kategori, "Transportasi")

    def test_total_args(self):
        self.assertEqual(self.analisis.total(1000, 2000, 3000), 6000)

    def test_rekap_kategori(self):
        daftar = [
            Pengeluaran("2026-10-11", "Makan", "Roti", 5000),
            Pengeluaran("2026-10-11", "Makan", "Susu", 7000),
        ]
        self.assertEqual(self.analisis.total_per_kategori(daftar)["Makan"], 12000)

    def test_file_tambah_dan_baca(self):
        self.file_data.buat_file()
        self.file_data.tambah(Pengeluaran("2026-10-11", "Makan", "Roti", 5000))
        self.assertEqual(len(self.file_data.baca_semua()), 1)

    def test_validasi_nominal(self):
        self.assertEqual(validasi_nominal("25000"), 25000)

    def test_validasi_tanggal_salah(self):
        with self.assertRaises(ValueError):
            validasi_tanggal("11-10-2026")

if __name__ == "__main__":
    unittest.main()
