import tkinter as tk

def hisoblash():
    try:
        natija = eval(kirish.get())
        kirish.delete(0, tk.END)
        kirish.insert(0, str(natija))
    except:
        kirish.delete(0, tk.END)
        kirish.insert(0, "XATO")

# Asosiy oyna
oyna = tk.Tk()
oyna.title("Sodda Kalkulyator")
oyna.geometry("250x150")

# Kirish maydoni
kirish = tk.Entry(oyna, font=("Arial", 16), justify="center")
kirish.pack(pady=10, padx=10, fill="x")

# Hisoblash tugmasi
tugma = tk.Button(oyna, text="HISOBLASH", font=("Arial", 14),
                  command=hisoblash, bg="lightblue")
tugma.pack(pady=10)

# Yordam matni
yordam = tk.Label(oyna, text="Misol: 2+3*4 yoki 10/2-1",
                  font=("Arial", 10), fg="gray")
yordam.pack()

# Dasturni ishga tushirish
oyna.mainloop()