def input_int(teks):
    while True:
        try:
            return int(input(teks))
        except ValueError:
            print("Masukkan angka yang valid!")

def input_bool(teks):
    return input(teks + " (y/n): ").lower() == 'y'


def hitung_faraidh():
    print("=== KALKULATOR WARIS ISLAM (FARAIDH) ===")

    harta = float(input("Total harta (setelah hutang & wasiat): "))

    # Input ahli waris
    istri = input_int("Jumlah istri: ")

    ibu = input_bool("Apakah ada ibu?")
    ayah = input_bool("Apakah ada ayah?")

    anak_lk = input_int("Jumlah anak laki-laki: ")
    anak_pr = input_int("Jumlah anak perempuan: ")

    bagian = {}
    total_bagian = 0

    # ======================
    # ISTRI
    # ======================
    if istri > 0:
        if anak_lk + anak_pr > 0:
            bagian['istri'] = 1/8
        else:
            bagian['istri'] = 1/4
        total_bagian += bagian['istri']

    # ======================
    # IBU
    # ======================
    if ibu:
        if anak_lk + anak_pr > 0:
            bagian['ibu'] = 1/6
        else:
            bagian['ibu'] = 1/3
        total_bagian += bagian['ibu']

    # ======================
    # AYAH
    # ======================
    if ayah:
        if anak_lk + anak_pr > 0:
            bagian['ayah'] = 1/6
            total_bagian += bagian['ayah']
        else:
            bagian['ayah'] = 0  # nanti ambil sisa

    # ======================
    # ANAK
    # ======================
    sisa = 1 - total_bagian

    if sisa < 0:
        # AUL (penyusutan)
        print("\nTerjadi AUL (penyusutan bagian)")
        for k in bagian:
            bagian[k] = bagian[k] / total_bagian
        sisa = 0

    hasil = {}

    # hitung nilai rupiah bagian tetap
    for k in bagian:
        hasil[k] = bagian[k] * harta

    # ======================
    # SISA KE ANAK (ASHABAH)
    # ======================
    if anak_lk + anak_pr > 0 and sisa > 0:
        total_unit = (anak_lk * 2) + anak_pr

        if total_unit > 0:
            nilai_per_unit = (sisa * harta) / total_unit

            if anak_lk > 0:
                hasil['anak_laki'] = nilai_per_unit * 2
            if anak_pr > 0:
                hasil['anak_perempuan'] = nilai_per_unit

    # ======================
    # AYAH AMBIL SISA (jika tidak ada anak)
    # ======================
    if ayah and anak_lk + anak_pr == 0:
        hasil['ayah'] = hasil.get('ayah', 0) + (sisa * harta)

    # ======================
    # OUTPUT
    # ======================
    print("\n=== HASIL PEMBAGIAN ===")
    for k, v in hasil.items():
        print(f"{k} : Rp {v:,.2f}")


if __name__ == "__main__":
    hitung_faraidh()
