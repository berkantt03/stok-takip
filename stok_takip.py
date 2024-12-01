import tkinter as tk
from tkinter import messagebox

# Yığın (Stack) fonksiyonları
degisiklikler = []  # Son değişikliklerin yığını

def is_empty():
    return len(degisiklikler) == 0

def push(item):
    degisiklikler.append(item)

def pop():
    if not is_empty():
        return degisiklikler.pop()
    else:
        return None


# Stok verilerini tutmak için sözlük ve liste
stok = {}
urun_sirasi = []

# Ürün ekleme ve güncelleme fonksiyonu
def urun_ekle(urun_adi, stok_miktari):
    if urun_adi in stok:
        push((urun_adi, stok[urun_adi]))  # Önceki değeri sakla
    else:
        push((urun_adi, None))  # Yeni ürün
        urun_sirasi.append(urun_adi)
    stok[urun_adi] = stok_miktari
    messagebox.showinfo("Başarılı", f"{urun_adi} eklendi/güncellendi, stok miktarı: {stok_miktari}")

# Geri alma fonksiyonu
def geri_al():
    if is_empty():
        messagebox.showinfo("Bilgi", "Geri alınacak işlem yok.")
        return
    urun_adi, eski_miktar = pop()
    if eski_miktar is None:
        urun_sirasi.remove(urun_adi)
        del stok[urun_adi]
        messagebox.showinfo("Geri Alma", f"{urun_adi} geri alındı (ürün silindi).")
    else:
        stok[urun_adi] = eski_miktar
        messagebox.showinfo("Geri Alma", f"{urun_adi} geri alındı, stok miktarı eski hale getirildi: {eski_miktar}")

# Sıralı stok listeleme fonksiyonu
def stok_listele():
    if not urun_sirasi:
        messagebox.showinfo("Stok Bilgisi", "Stokta ürün yok.")
    else:
        stok_listesi = "\n".join([f"{urun}: {stok[urun]} adet" for urun in urun_sirasi])
        messagebox.showinfo("Stok Listesi", stok_listesi)

# Tkinter Arayüzü
root = tk.Tk()
root.title("Stok Takip Uygulaması")

# Ürün Adı Girişi
urun_adi_label = tk.Label(root, text="Ürün Adı:")
urun_adi_label.grid(row=0, column=0, padx=10, pady=5)
urun_adi_entry = tk.Entry(root)
urun_adi_entry.grid(row=0, column=1, padx=10, pady=5)

# Stok Miktarı Girişi
stok_miktari_label = tk.Label(root, text="Stok Miktarı:")
stok_miktari_label.grid(row=1, column=0, padx=10, pady=5)
stok_miktari_entry = tk.Entry(root)
stok_miktari_entry.grid(row=1, column=1, padx=10, pady=5)

# Ürün Ekle/Güncelle Butonu
def urun_ekle_buton():
    urun_adi = urun_adi_entry.get()
    stok_miktari = stok_miktari_entry.get()
    if urun_adi and stok_miktari.isdigit():
        urun_ekle(urun_adi, int(stok_miktari))
        urun_adi_entry.delete(0, tk.END)
        stok_miktari_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Hata", "Lütfen geçerli bir ürün adı ve stok miktarı girin.")

urun_ekle_button = tk.Button(root, text="Ürün Ekle/Güncelle", command=urun_ekle_buton)
urun_ekle_button.grid(row=2, column=0, columnspan=2, pady=10)

# Stokları Listele Butonu
stok_listele_button = tk.Button(root, text="Stokları Listele", command=stok_listele)
stok_listele_button.grid(row=3, column=0, columnspan=2, pady=5)

# Geri Al Butonu
geri_al_button = tk.Button(root, text="Geri Al", command=geri_al)
geri_al_button.grid(row=4, column=0, columnspan=2, pady=5)

# Çıkış Butonu
def cikis():
    root.quit()

cikis_button = tk.Button(root, text="Çıkış", command=cikis)
cikis_button.grid(row=5, column=0, columnspan=2, pady=10)

# Arayüzü Başlat
root.mainloop()
