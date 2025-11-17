import tkinter as tk
import calendar
class mycalendar:
    def __init__(self, master):
        self.master = master
        master.title("Kalenderku")
        master.geometry("400x400")
        self.frame_utama = tk.Frame(master)
        self.frame_utama.pack(pady=15)
        self.label_tahun = tk.Label(self.frame_utama, text="Tahun:")
        self.label_tahun.grid(row=0, column=0)
        self.entry_tahun = tk.Entry(self.frame_utama)
        self.entry_tahun.grid(row=0, column=1)
        self.label_bulan = tk.Label(self.frame_utama, text="Bulan (1-12):")
        self.label_bulan.grid(row=1, column=0)
        self.entry_bulan = tk.Entry(self.frame_utama)
        self.entry_bulan.grid(row=1, column=1)
        self.btn_display = tk.Button(self.frame_utama, text="Tampilkan Kalender", command=self.tampilkan_kalender)
        self.btn_display.grid(row=2, column=0, columnspan=2, pady=10)
        self.canvas = tk.Canvas(master, width=100, height=100, bg="lightgray")
        self.canvas.pack(pady=10)
        self.canvas.create_polygon(50, 20, 20, 80, 80, 80, fill="skyblue")  
        self.text_kalender = tk.Text(master, height=8, width=30)
        self.text_kalender.pack()

    def tampilkan_kalender(self):
        try:
            tahun = int(self.entry_tahun.get())
            bulan = int(self.entry_bulan.get())
            if 1 <= bulan <= 12:
                hasil = calendar.month(tahun, bulan)
                self.text_kalender.delete("1.0", tk.END)
                self.text_kalender.insert(tk.END, hasil)
            else:
                self.text_kalender.delete("1.0", tk.END)
                self.text_kalender.insert(tk.END, "Bulan harus antara 1 dan 12.")
        except ValueError:
            self.text_kalender.delete("1.0", tk.END)
            self.text_kalender.insert(tk.END, "Masukkan angka yang valid.")

# Menjalankan program
if __name__ == "__main__":
    root = tk.Tk()
    app = mycalendar(root)
    root.mainloop()