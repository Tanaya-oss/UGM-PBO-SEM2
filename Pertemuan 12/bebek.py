import tkinter as tk
from tkinter import messagebox

def hitung_emisi():
    try:
        # Konstanta: faktor emisi karbon (gram CO2 per Wh)
        # Nilai ini bervariasi tergantung sumber energi, contoh menggunakan rata-rata grid listrik
        FAKTOR_EMISI = 0.85  # gram CO2 per Wh (contoh untuk Indonesia)
        
        # Ambil nilai dari input
        daya = float(daya_entry.get())          # dalam Watt
        jumlah = int(jumlah_entry.get())        # jumlah perangkat
        durasi = float(durasi_entry.get())      # jam per hari
        frekuensi = float(frekuensi_entry.get()) # hari per minggu
        
        # Hitung konsumsi energi dalam Wh per minggu
        energi_wh = daya * jumlah * durasi * frekuensi
        
        # Hitung emisi karbon dalam gram CO2
        emisi = energi_wh * FAKTOR_EMISI
        
        # Konversi ke kg CO2 untuk tampilan
        emisi_kg = emisi / 1000
        
        # Tampilkan hasil
        hasil_text = (
            f"Konsumsi Energi: {energi_wh:.2f} Wh/minggu\n"
            f"Emisi Karbon: {emisi:.2f} g CO2/minggu\n"
            f"({emisi_kg:.3f} kg CO2/minggu)\n\n"
            f"*Berdasarkan faktor emisi {FAKTOR_EMISI} g CO2/Wh"
        )
        hasil_label.config(text=hasil_text)
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid di semua field!")

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Emisi Karbon Elektronik")
root.geometry("400x400")

# Style
root.configure(bg='#f0f0f0')
font_label = ('Arial', 10)
font_entry = ('Arial', 10)
font_button = ('Arial', 10, 'bold')
font_hasil = ('Arial', 10)

# Judul
title_label = tk.Label(root, 
                      text="Kalkulator Emisi Karbon Perangkat Elektronik",
                      font=('Arial', 12, 'bold'),
                      bg='#f0f0f0')
title_label.pack(pady=10)

# Frame untuk input
input_frame = tk.Frame(root, bg='#f0f0f0')
input_frame.pack(pady=10)

# Label dan Entry untuk Daya Perangkat
tk.Label(input_frame, 
        text="Daya Perangkat (Watt):", 
        font=font_label,
        bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5, sticky='e')
daya_entry = tk.Entry(input_frame, font=font_entry)
daya_entry.grid(row=0, column=1, padx=5, pady=5)

# Label dan Entry untuk Jumlah Perangkat
tk.Label(input_frame, 
        text="Jumlah Perangkat:", 
        font=font_label,
        bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=5, sticky='e')
jumlah_entry = tk.Entry(input_frame, font=font_entry)
jumlah_entry.grid(row=1, column=1, padx=5, pady=5)

# Label dan Entry untuk Durasi
tk.Label(input_frame, 
        text="Durasi Penggunaan (jam/hari):", 
        font=font_label,
        bg='#f0f0f0').grid(row=2, column=0, padx=5, pady=5, sticky='e')
durasi_entry = tk.Entry(input_frame, font=font_entry)
durasi_entry.grid(row=2, column=1, padx=5, pady=5)

# Label dan Entry untuk Frekuensi
tk.Label(input_frame, 
        text="Frekuensi Penggunaan (hari/minggu):", 
        font=font_label,
        bg='#f0f0f0').grid(row=3, column=0, padx=5, pady=5, sticky='e')
frekuensi_entry = tk.Entry(input_frame, font=font_entry)
frekuensi_entry.grid(row=3, column=1, padx=5, pady=5)

# Tombol Hitung
hitung_button = tk.Button(root, 
                         text="Hitung Emisi Karbon", 
                         command=hitung_emisi,
                         font=font_button,
                         bg='#4CAF50',
                         fg='white',
                         padx=10,
                         pady=5)
hitung_button.pack(pady=15)

# Frame untuk hasil
hasil_frame = tk.Frame(root, bg='#e9f7ef', bd=2, relief=tk.GROOVE)
hasil_frame.pack(pady=10, padx=20, fill=tk.BOTH)

hasil_label = tk.Label(hasil_frame, 
                      text="Hasil akan muncul di sini...", 
                      font=font_hasil,
                      bg='#e9f7ef',
                      justify=tk.LEFT)
hasil_label.pack(pady=10, padx=10)

# Catatan kaki
catatan_label = tk.Label(root, 
                        text="*Faktor emisi dapat bervariasi tergantung sumber energi listrik di daerah Anda",
                        font=('Arial', 8),
                        bg='#f0f0f0',
                        fg='#555555')
catatan_label.pack(pady=5)

root.mainloop()