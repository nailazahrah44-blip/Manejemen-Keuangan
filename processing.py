class Pengeluaran:
    """Mewakili satu catatan pengeluaran."""

    def __init__(self, tanggal, kategori, keterangan, nominal):
        if not tanggal.strip():
            raise ValueError("Tanggal tidak boleh kosong.")

        if not kategori.strip():
            raise ValueError("Kategori tidak boleh kosong.")

        if not keterangan.strip():
            raise ValueError("Keterangan tidak boleh kosong.")

        nominal = float(nominal)

        if nominal <= 0:
            raise ValueError("Nominal harus lebih dari nol.")

        self.tanggal = tanggal.strip()
        self.kategori = kategori.strip()
        self.keterangan = keterangan.strip()
        self.nominal = nominal

    def ke_baris(self):
        """Mengubah catatan menjadi satu baris teks."""
        return (
            f"{self.tanggal}|{self.kategori}|"
            f"{self.keterangan}|{self.nominal}"
        )

    @classmethod
    def dari_baris(cls, baris):
        """Membaca satu baris teks menjadi objek pengeluaran."""
        bagian = baris.strip().split("|")

        if len(bagian) != 4:
            raise ValueError("Format data tidak sesuai.")

        return cls(
            bagian[0],
            bagian[1],
            bagian[2],
            float(bagian[3])
        )


class PengelolaPengeluaran:
    """Mengelola pembuatan catatan pengeluaran."""

    def buat_catatan(self, **kwargs):
        wajib = {
            "tanggal",
            "kategori",
            "keterangan",
            "nominal"
        }

        if not wajib.issubset(kwargs):
            raise ValueError("Data pengeluaran belum lengkap.")

        return Pengeluaran(
            tanggal=kwargs["tanggal"],
            kategori=kwargs["kategori"],
            keterangan=kwargs["keterangan"],
            nominal=float(kwargs["nominal"])
        )
