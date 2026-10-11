from datetime import datetime

def validasi_tanggal(tanggal):
    """Memastikan tanggal menggunakan format YYYY-MM-DD."""
    try:
        tanggal_obj = datetime.strptime(tanggal, "%Y-%m-%d")

        if tanggal_obj.strftime("%Y-%m-%d") != tanggal:
            raise ValueError

    except ValueError:
        raise ValueError(
            "Format tanggal harus YYYY-MM-DD, "
            "contoh: 2026-10-11."
        )

    return tanggal

def validasi_nominal(nominal):
    """Memastikan nominal berupa angka positif."""
    try:
        nilai = float(nominal)
    except (ValueError, TypeError):
        raise ValueError("Nominal harus berupa angka.")

    if nilai <= 0:
        raise ValueError("Nominal harus lebih dari nol.")

    return nilai
