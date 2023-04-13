class Item:
    def __init__(self, name, tipe, price):
        self.name = name
        self.tipe = tipe
        self.price = price

class HPStore:
    def __init__(self):
        self.items = [Item('Samsung', 'A10     ', 1000000), Item('Samsung', 'A15     ', 1500000), Item('Samsung', 'A25     ', 2000000), 
                      Item('Xiaomi ', 'Redmi 9 ', 1200000), Item('Xiaomi ','Redmi 10', 1800000), Item('Xiaomi ', 'Redmi 11', 2100000), 
                      Item('OPPO   ','A1      ', 1000000 ), Item('OPPO   ','A14     ', 1700000), Item('OPPO   ', 'Reno    ', 2200000)]
        
    def show_items(self):
        print("==========================================")
        print("|       Selamat Datang di HP Store       |")
        print("==========================================")
        print("|        Daftar HP yang tersedia:        |")
        print("==========================================")
        print("|    Merk     |   Tipe    |    Harga     |")
        print("==========================================")

        for i, item in enumerate(self.items):
            print(f"| {i+1}. {item.name}  |  {item.tipe} |- Rp. {item.price}  |")
        print("==========================================\n")
        
    def buy(self, username):
        print(f"\nHallo, {username}! \n")
        self.show_items()
        
        total_price = 0
        selected_items = []
        total_item = 0
    
        while True:
            selected = input("Pilih nomor barang yang ingin dibeli (0 untuk selesai): ")
            if selected == '0':
                break
            
            try:
                selected_item = self.items[int(selected)-1]
            except:
                print("Mohon masukkan nomor barang yang valid!")
                continue
                
            quantity = int(input("Jumlah barang yang ingin dibeli: "))
            
            total_price += selected_item.price * quantity
            selected_items.append((selected_item, quantity))
            
            print(f"Barang '{selected_item.name}' sebanyak {quantity} buah telah ditambahkan ke keranjang belanja.\n")
            total_item += quantity

        print(f"\nTotal harga: Rp {total_price}")
        payment = int(input("Masukkan jumlah uang pembayaran: "))
        
        while payment < total_price:
            print("Maaf, uang pembayaran Anda kurang!")
            payment = int(input("Masukkan jumlah uang pembayaran: "))
            
        change = payment - total_price
        
        if change > 0:
            print(f"\nTotal Item: {total_item}")
            print(f"\nTotal Belanja: Rp {total_price}")
            print(f"\nTunai: Rp {payment}")
            print(f"\nKembalian: Rp {change}")
            
        print("\nTerima kasih telah berbelanja di HP Store!")
        
        if input("Apakah Anda ingin membeli lagi? (y/t): ") == 'y':
            main()
        else:
            print("Program selesai.")
            

def main():
    print("=== HP Store ===\n")
    username = input("Masukkan nama Anda: ")
    
    hp_store = HPStore()
    hp_store.buy(username)
    
if __name__ == '__main__':
    main()
