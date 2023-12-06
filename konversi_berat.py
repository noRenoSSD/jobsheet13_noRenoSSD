def weight_conversion():
    berat = int(input("Masukkan angka: "))
    satuan = input("Dalam satuan apa berat yang anda masukkan?" ("K untuk KG dan L untuk LBS"))
    if satuan.lower()=='l':
        print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)}kg")

    elif satuan.lower()=='k':
        print(f"Berat anda dikonfresi menjadi pons adalah {round(berat*2.20462)}lbs")