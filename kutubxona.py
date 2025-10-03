# Kitoblar topish

kitoblar = {
    "Clean Code": 120_000,
    "Python Crash Course": 150_000,
    "Introduction to Algorithms": 350_000,
    "Fluent Python": 210_000,
}

title = input("Kitob nomini kiriting: ")

title_lower = title.strip().lower()
top = False

for nomi, narx in kitoblar.items():
    if nomi.lower() == title_lower:
        print(f"'{nomi}' - kitobi narxi: {narx} so'm")
        top = True
        break

if not top:
    print("Kitob topilmadi.")


# Ko'paytirish jadvali (1 dan 9 gacha)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:3}", end=" ")
    print()

# Ai,j​=a1​+d⋅((i−1)⋅n+(j−1))