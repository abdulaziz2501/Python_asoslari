import tkinter as tk
from tkinter import messagebox


class Kalkulyator:
    def __init__(self):
        self.oyna = tk.Tk()
        self.oyna.title("Python Kalkulyator")
        self.oyna.geometry("350x400")
        self.oyna.resizable(False, False)

        # Natija ko'rsatish uchun o'zgaruvchi
        self.natija_var = tk.StringVar()
        self.natija_var.set("0")

        self.interfeys_yaratish()

    def interfeys_yaratish(self):
        # Natija ko'rsatish maydoni
        natija_label = tk.Label(
            self.oyna,
            textvariable=self.natija_var,
            font=("Arial", 20),
            bg="white",
            relief="sunken",
            anchor="e",
            padx=10
        )
        natija_label.pack(fill="x", padx=10, pady=10)

        # Tugmalar ramkasi
        tugmalar_ramka = tk.Frame(self.oyna)
        tugmalar_ramka.pack(padx=10, pady=5)

        # Tugmalar matritsasi
        tugmalar = [
            ['C', '÷', '×', '←'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '', '']
        ]

        # Tugmalarni yaratish
        for i, qator in enumerate(tugmalar):
            for j, tugma_text in enumerate(qator):
                if tugma_text:
                    if tugma_text == '0':
                        # Nol tugmasi kengroq
                        tugma = tk.Button(
                            tugmalar_ramka,
                            text=tugma_text,
                            font=("Arial", 14),
                            width=10,
                            height=2,
                            command=lambda t=tugma_text: self.tugma_bosildi(t)
                        )
                        tugma.grid(row=i, column=j, columnspan=2,
                                   padx=2, pady=2, sticky="ew")
                    elif tugma_text == '=':
                        # Teng tugmasi balandroq
                        tugma = tk.Button(
                            tugmalar_ramka,
                            text=tugma_text,
                            font=("Arial", 14),
                            width=5,
                            height=4,
                            bg="orange",
                            command=self.hisoblash
                        )
                        tugma.grid(row=i, column=j, rowspan=2,
                                   padx=2, pady=2, sticky="ns")
                    else:
                        # Oddiy tugmalar
                        tugma = tk.Button(
                            tugmalar_ramka,
                            text=tugma_text,
                            font=("Arial", 14),
                            width=5,
                            height=2,
                            command=lambda t=tugma_text: self.tugma_bosildi(t)
                        )
                        tugma.grid(row=i, column=j, padx=2, pady=2)

    def tugma_bosildi(self, qiymat):
        joriy = self.natija_var.get()

        if qiymat == 'C':
            # Tozalash
            self.natija_var.set("0")
        elif qiymat == '←':
            # Oxirgi belgini o'chirish
            if len(joriy) > 1:
                self.natija_var.set(joriy[:-1])
            else:
                self.natija_var.set("0")
        elif qiymat in ['+', '-', '×', '÷']:
            # Amal belgilari
            if joriy != "0" and joriy[-1] not in ['+', '-', '×', '÷']:
                if qiymat == '×':
                    self.natija_var.set(joriy + '*')
                elif qiymat == '÷':
                    self.natija_var.set(joriy + '/')
                else:
                    self.natija_var.set(joriy + qiymat)
        else:
            # Sonlar va nuqta
            if joriy == "0":
                self.natija_var.set(qiymat)
            else:
                self.natija_var.set(joriy + qiymat)

    def hisoblash(self):
        try:
            ifoda = self.natija_var.get()
            if any(char in ifoda for char in ['+', '-', '*', '/']):
                natija = eval(ifoda)
                self.natija_var.set(str(natija))
            else:
                messagebox.showerror("Xato", "Yaroqsiz ifoda!")
        except ZeroDivisionError:
            messagebox.showerror("Xato", "Nolga bo'lish mumkin emas!")
        except:
            messagebox.showerror("Xato", "Hisoblashda xato yuz berdi!")

    def ishga_tushirish(self):
        self.oyna.mainloop()


# Dasturni ishga tushirish
if __name__ == "__main__":
    kalkulyator = Kalkulyator()

    kalkulyator.ishga_tushirish()