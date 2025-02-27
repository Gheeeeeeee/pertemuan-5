class PersegiPanjang:
    def init(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def menghitung_luas(self):
        return self.panjang * self.lebar
    
    def str(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    

def main():
    print("=== Program Persegi Panjang ===")
    
    try:
        # Meminta input panjang dan lebar dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
        # Validasi input
        if panjang <= 0 or lebar <= 0:
            print("Panjang dan lebar harus bernilai positif!")
            return

        # Membuat objek PersegiPanjang
        persegi_panjang = PersegiPanjang(panjang, lebar)
        
        # Menampilkan informasi dan hasil perhitungan
        print("\n=== Hasil Perhitungan ===")
        print(persegi_panjang)
        print("Keliling:", persegi_panjang.keliling(), "cm")
        print("Luas:", persegi_panjang.menghitung_luas(), "cm²")
        
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

# Menjalankan program utama
main()